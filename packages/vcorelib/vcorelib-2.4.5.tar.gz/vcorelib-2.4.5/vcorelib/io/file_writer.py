"""
A module implementing an interface for writing to variably indented files.
"""

# built-in
from contextlib import contextmanager
from io import StringIO
from os import linesep
from pathlib import Path
from typing import Iterator, TextIO

# internal
from vcorelib import DEFAULT_ENCODING
from vcorelib.paths.context import tempfile


class IndentedFileWriter:
    """A class for writing lines to a file and tracking indentation."""

    def __init__(
        self,
        stream: TextIO,
        space: str = " ",
        per_indent: int = 1,
        prefix: str = "",
        suffix: str = "",
    ) -> None:
        """Initialize this instance."""

        self.stream = stream
        self.space = space
        self.per_indent = per_indent
        self.depth = 0

        self._prefix = prefix
        self._suffix = suffix

    @contextmanager
    def prefix(self, prefix: str) -> Iterator[None]:
        """Set a new line prefix as a managed context."""

        curr = self._prefix
        self._prefix = prefix
        try:
            yield
        finally:
            self._prefix = curr

    @contextmanager
    def suffix(self, suffix: str) -> Iterator[None]:
        """Set a new line suffix as a managed context."""

        curr = self._suffix
        self._suffix = suffix
        try:
            yield
        finally:
            self._suffix = curr

    @contextmanager
    def ends(self, prefix: str = "", suffix: str = "") -> Iterator[None]:
        """Adds a temporary prefix and suffix to lines."""
        with self.prefix(prefix):
            with self.suffix(suffix):
                yield

    @staticmethod
    @contextmanager
    def from_path(
        path: Path, space: str = " ", per_indent: int = 1
    ) -> Iterator["IndentedFileWriter"]:
        """Create an instance from a path as a managed context."""

        with path.open("w", encoding=DEFAULT_ENCODING) as stream:
            yield IndentedFileWriter(
                stream, space=space, per_indent=per_indent
            )

    @staticmethod
    @contextmanager
    def string(
        space: str = " ", per_indent: int = 1
    ) -> Iterator["IndentedFileWriter"]:
        """Create an instance for a string."""

        with StringIO() as stream:
            yield IndentedFileWriter(
                stream, space=space, per_indent=per_indent
            )

    @staticmethod
    @contextmanager
    def temporary(
        space: str = " ", per_indent: int = 1
    ) -> Iterator["IndentedFileWriter"]:
        """Create an instance from a temporary file as a managed context."""

        with tempfile() as tmp:
            with IndentedFileWriter.from_path(
                tmp, space=space, per_indent=per_indent
            ) as writer:
                yield writer

    def write(self, data: str) -> int:
        """
        method taking the str data for a new line of text to write
        to the file: first writes the indent (some number of
        e.g. space characters), then writes the str data (function parameter),
        then writes a newline character (os.linesep).
        """

        data = (
            (self.space * self.depth * self.per_indent)
            + self._prefix
            + data
            + self._suffix
            + linesep
        )
        self.stream.write(data)
        return len(data)

    def cpp_comment(self, data: str) -> int:
        """A helper for writing C++-style comments."""
        return self.write("// " + data)

    def c_comment(self, data: str) -> int:
        """A helper for writing C-style comments."""

        with self.ends("/* ", " */"):
            result = self.write(data)
        return result

    def indent(self, amount: int = 1) -> None:
        """Increase the current indent depth."""

        self.depth += amount

    def dedent(self, amount: int = 1) -> None:
        """Decrease the current indent depth (if not zero)."""

        if self.depth > 0 and amount <= self.depth:
            self.depth -= amount

    @contextmanager
    def indented(self, amount: int = 1) -> Iterator[None]:
        """Increase the current indent depth and decrease upon exit."""

        self.indent(amount=amount)
        try:
            yield
        finally:
            self.dedent(amount=amount)

    @contextmanager
    def scope(
        self,
        opener: str = "{",
        closer: str = "}",
        prefix: str = "",
        suffix: str = "",
        indent: int = 1,
    ) -> Iterator[None]:
        """A helper for common programming syntax scoping."""

        self.write(prefix + opener)
        with self.indented(amount=indent):
            yield
        self.write(closer + suffix)

    @contextmanager
    def javadoc(
        self, opener: str = "/**", closer: str = " */", prefix: str = " * "
    ) -> Iterator[None]:
        """A helper for writing javadoc-style comments."""

        with self.scope(opener=opener, closer=closer, indent=0):
            with self.prefix(prefix):
                yield
