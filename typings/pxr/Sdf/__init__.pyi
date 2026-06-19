"""Minimal local stubs for pxr.Sdf while learning USD."""

from typing import Any


class Layer:
    identifier: str
    realPath: str
    subLayerPaths: list[str]

    @staticmethod
    def CreateNew(identifier: str, args: dict[str, Any] | None = None) -> "Layer": ...

    @staticmethod
    def Find(identifier: str) -> "Layer | None": ...

    @staticmethod
    def FindOrOpen(identifier: str) -> "Layer | None": ...

    def Export(self, filePath: str, comment: str = "", args: dict[str, Any] | None = None) -> bool: ...
    def ExportToString(self) -> str: ...
    def Save(self, force: bool = False) -> bool: ...


def Find(layerFileName: str, scenePath: Any = ...) -> Any: ...