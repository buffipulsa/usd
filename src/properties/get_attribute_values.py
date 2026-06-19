from pxr import Usd, UsdGeom, Gf

import src.tools.path_tools as path_tools


root_path = path_tools.find_repo_root()
file_path = root_path / "out" / "attributes_ex2.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(str(file_path))

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(
    stage, world_xform.GetPath().AppendPath("Sphere")
)

cube: UsdGeom.Cube = UsdGeom.Cube.Define(
    stage, world_xform.GetPath().AppendPath("Cube")
)

UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))

cube_attrs = cube.GetPrim().GetAttributes()
for attr in cube_attrs:
    print(attr)

cube_size: Usd.Attribute = cube.GetSizeAttr()
cube_display_color: Usd.Attribute = cube.GetDisplayColorAttr()
cube_extent: Usd.Attribute = cube.GetExtentAttr()

print("Size: ", cube_size.Get())
print("Display color : ", cube_display_color.Get())
print("Extent: ", cube_extent.Get())

stage.Save()
