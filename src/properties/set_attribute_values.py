from pxr import Usd, UsdGeom, Gf

import src.tools.path_tools as path_tools


root_path = path_tools.find_repo_root()
file_path = root_path / "out" / "attributes_ex3.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(str(file_path))

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(
    stage, world_xform.GetPath().AppendPath("Sphere")
)

cube: UsdGeom.Cube = UsdGeom.Cube.Define(
    stage, world_xform.GetPath().AppendPath("Cube")
)

UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))

cube_size: Usd.Attribute = cube.GetSizeAttr()
cube_display_color: Usd.Attribute = cube.GetDisplayColorAttr()
cube_extent: Usd.Attribute = cube.GetExtentAttr()

cube_size.Set(cube_size.Get() * 2)
cube_extent.Set(cube_extent.Get() * 2)
cube_display_color.Set([(0.0, 1.0, 0.0)])

stage.Save()

print(stage.ExportToString(addSourceFileComment=False))
