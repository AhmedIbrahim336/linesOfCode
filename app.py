import os 
from constants import ROOT_DIR
from project import project_metadata, analizeProject
from utils import display_project
from pprint import pprint

projects_list = os.listdir(ROOT_DIR)

for project in projects_list:
    metadata = project_metadata(project)
    result = analizeProject(project)
    metadata['stack'] = result
    display_project(metadata)
    # pprint(metadata)
