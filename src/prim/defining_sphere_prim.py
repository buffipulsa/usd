"""Define a sphere prim and author its radius attribute.

This module creates ``out/sphere_prim.usda``, defines a ``UsdGeom.Sphere`` at
``/hello``, authors a radius of ``2``, then saves and prints the stage.

Notes
-----
Using the ``UsdGeom.Sphere`` schema provides typed accessors such as
``CreateRadiusAttr`` instead of requiring a generic attribute lookup.
"""

from pxr import Usd, UsdGeom

import src.tools.path_tools as path_tools


root_path = path_tools.find_repo_root()
file_path = root_path / "out" / "sphere_prim.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(str(file_path))

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, "/hello")
sphere.CreateRadiusAttr().Set(2)

stage.Save()

print(stage.ExportToString(addSourceFileComment=False))
