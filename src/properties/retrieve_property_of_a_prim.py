"""List the property names available on a prim.

This module creates ``out/attributes_ex1.usda``, defines a sphere and translated
cube below ``/World``, and prints the cube's property names before saving the
stage.

Notes
-----
``Usd.Prim.GetPropertyNames`` returns the names of both attributes and
relationships composed on the prim. It does not return the property objects.
"""

from pxr import Usd, UsdGeom, Gf

import src.tools.path_tools as path_tools


root_path = path_tools.find_repo_root()
file_path = root_path / "out" / "attributes_ex1.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(str(file_path))

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(
    stage, world_xform.GetPath().AppendPath("Sphere")
)

cube: UsdGeom.Cube = UsdGeom.Cube.Define(
    stage, world_xform.GetPath().AppendPath("Cube")
)

UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))

cube_prop_names = cube.GetPrim().GetPropertyNames()

for prop_name in cube_prop_names:
    print(prop_name)

stage.Save()

print(stage.ExportToString(addSourceFileComment=False))
