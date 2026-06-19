
from pxr import Usd

import src.tools.path_tools as path_tools

root_path = path_tools.find_repo_root()

file_path = root_path / 'out' / 'first_stage.usda'

stage: Usd.Stage = Usd.Stage.CreateNew(str(file_path))
print(stage.ExportToString(addSourceFileComment=False))