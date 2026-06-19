
from pxr import Usd

import src.tools.path_tools as path_tools

stage: Usd.Stage = Usd.Stage.CreateInMemory()

stage.DefinePrim('/World', 'Xform')

print(
    'In-memory stage: ',
    stage.ExportToString(addSourceFileComment=False)
)

root_path = path_tools.find_repo_root()

file_path = root_path / 'out' / 'in_memory_stage.usda'

stage.Export(str(file_path))