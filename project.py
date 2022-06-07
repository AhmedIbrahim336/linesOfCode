import os 
import pathlib
import json

from constants import ROOT_DIR
from utils import is_default_file, get_file_type

def project_metadata(project):
    project_json = os.path.join(ROOT_DIR, project, 'project.json')
    path = pathlib.Path(project_json)

    if not path.exists():
        print('%s doesn\'t have project.json file!')
        return
    
    with open(project_json, 'rt') as f:
        json_str = f.read()
        metadata = json.loads(json_str)
    
    return metadata

def analizeProject(project: str):
    project_path = pathlib.Path(os.path.join(ROOT_DIR, project))
    project_files = os.listdir(project_path)
    
    result = {}

    for file in project_files:
        file_path = pathlib.Path(os.path.join(project_path, file))

        if file_path.is_dir() or is_default_file(file):
            continue

        with open(file_path, 'rt') as f:
            file_type = get_file_type(file)
            num_of_lines = len(f.readlines())

            if result.get(file_type, None):
                result[file_type] = result[file_type] + num_of_lines
            else:
                result[file_type] = num_of_lines
    return result


