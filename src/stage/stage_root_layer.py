
from pxr import Usd, Sdf

import src.tools.path_tools as path_tools

root_path = path_tools.find_repo_root()

root_layer_path = root_path / 'out' / 'root_layer_example.usda' 

stage: Usd.Stage = Usd.Stage.CreateNew(str(root_layer_path))

root_layer: Sdf.Layer = stage.GetRootLayer()

stage.DefinePrim('/World', 'Xform')

extra_layer_path = root_path / 'out' / 'extra_layer.usdc' 
rel_path = extra_layer_path.relative_to(root_layer_path.parent)

extra_layer: Sdf.Layer = Sdf.Layer.CreateNew(str(extra_layer_path))

root_layer.subLayerPaths.append(str(rel_path.as_posix()))

stage.Save()
extra_layer.Save()

print(
    'Root layer contents: ',
    root_layer.ExportToString()
)