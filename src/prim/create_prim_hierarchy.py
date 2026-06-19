"""Create a hierarchy of typed geometry prims.

This module creates ``out/prim_hierarchy.usda`` and authors a ``Scope``, an
``Xform``, and a ``Cube`` at ``/Geometry/GroupTransform/Box``.

Notes
-----
``Sdf.Path.AppendPath`` builds each child path from its parent's path. A scope
organizes prims without adding a transform, while an xform can carry transform
operations for its descendants.
"""

from pxr import Usd, UsdGeom

import src.tools.path_tools as path_tools


root_path = path_tools.find_repo_root()
file_path = root_path / "out" / "prim_hierarchy.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(str(file_path))

geom_scope: UsdGeom.Scope = UsdGeom.Scope.Define(stage, "/Geometry")

xform: UsdGeom.Xform = UsdGeom.Xform.Define(
    stage,
    geom_scope.GetPath().AppendPath("GroupTransform"),
)

cube: UsdGeom.Cube = UsdGeom.Cube.Define(
    stage,
    xform.GetPath().AppendPath("Box"),
)

stage.Save()

print(stage.ExportToString(addSourceFileComment=False))
