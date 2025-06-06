import re
from collections.abc import Iterator, Mapping
from typing import IO, Any, ClassVar, Literal

from django.http.request import QueryDict
from django.utils.datastructures import ImmutableList, MultiValueDict

class MultiPartParserError(Exception): ...
class InputStreamExhausted(Exception): ...

RAW: Literal["raw"]
FILE: Literal["file"]
FIELD: Literal["field"]
FIELD_TYPES: frozenset[str]

class MultiPartParser:
    boundary_re: ClassVar[re.Pattern[str]]
    def __init__(
        self,
        META: Mapping[str, Any],
        input_data: IO[bytes],
        upload_handlers: list[Any] | ImmutableList[Any],
        encoding: str | None = ...,
    ) -> None: ...
    def parse(self) -> tuple[QueryDict, MultiValueDict]: ...
    def handle_file_complete(self, old_field_name: str, counters: list[int]) -> None: ...
    def sanitize_file_name(self, file_name: str) -> str | None: ...
    def IE_sanitize(self, file_name: str) -> str | None: ...

class LazyStream:
    length: int | None
    position: int
    def __init__(self, producer: BoundaryIter | ChunkIter, length: int | None = ...) -> None: ...
    def tell(self) -> int: ...
    def read(self, size: int | None = ...) -> bytes: ...
    def __next__(self) -> bytes: ...
    def close(self) -> None: ...
    def __iter__(self) -> LazyStream: ...
    def unget(self, bytes: bytes) -> None: ...

class ChunkIter:
    flo: IO[bytes]
    chunk_size: int
    def __init__(self, flo: IO[bytes], chunk_size: int = ...) -> None: ...
    def __next__(self) -> bytes: ...
    def __iter__(self) -> ChunkIter: ...

class InterBoundaryIter:
    def __init__(self, stream: LazyStream, boundary: bytes) -> None: ...
    def __iter__(self) -> InterBoundaryIter: ...
    def __next__(self) -> LazyStream: ...

class BoundaryIter:
    def __init__(self, stream: LazyStream, boundary: bytes) -> None: ...
    def __iter__(self) -> BoundaryIter: ...
    def __next__(self) -> bytes: ...

class Parser:
    def __init__(self, stream: LazyStream, boundary: bytes) -> None: ...
    def __iter__(self) -> Iterator[tuple[str, dict[str, tuple[str, dict[str, bytes | str]]], LazyStream]]: ...

__all__ = ("MultiPartParser", "MultiPartParserError", "InputStreamExhausted")
