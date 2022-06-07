import os 
import pathlib
import json
from pprint import pprint

from constants import ROOT_DIR
from utils import is_default_file, get_file_type

def project_metadata(project):
    project_json = os.path.join(ROOT_DIR, project, 'project.json')
    path = pathlib.Path(project_json)

    if not path.exists():
        print('%s doesn\'t have project.json file!')
        return dict()
    
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

def get_stats(projects):
    """
    Stats should include:
    1. Total lines of each tech 
    2. Percentage of each tech from the total stacked projects 
    3. Percentage of each tech from the each project 
    """

    freq_counter = dict()
    for project in projects:
        project_total_lines = 0
        for tech, lines in project.get('stack', {}).items():
            project_total_lines+=lines
            if freq_counter.get(tech, None):
                freq_counter[tech]+=lines
            else:
                 freq_counter[tech]=lines
        # Print stats for each project
        project_stat_str = ''
        for tech, lines in project.get('stack', {}).items():
            lines_per = (lines/project_total_lines) * 100
            project_stat_str+= '%.1f%% %s | ' % (lines_per, tech)
        
        print(project['name'], ":" , project_stat_str)

    
    pprint(freq_counter)
    
