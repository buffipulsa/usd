"""Minimal local stubs for pxr.UsdGeom while learning USD."""

from pxr import Sdf, Usd


class _SchemaBase:
    def GetPath(self) -> Sdf.Path: ...


class Scope(_SchemaBase):
    @staticmethod
    def Define(stage: Usd.Stage, path: Sdf.Path | str) -> "Scope": ...


class Xform(_SchemaBase):
    @staticmethod
    def Define(stage: Usd.Stage, path: Sdf.Path | str) -> "Xform": ...


class Cube(_SchemaBase):
    @staticmethod
    def Define(stage: Usd.Stage, path: Sdf.Path | str) -> "Cube": ...


class Sphere(_SchemaBase):
    @staticmethod
    def Define(stage: Usd.Stage, path: Sdf.Path | str) -> "Sphere": ...

    def CreateRadiusAttr(self, defaultValue: object = ...) -> Usd.Attribute: ...
