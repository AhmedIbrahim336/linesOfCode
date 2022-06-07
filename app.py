import os 
from constants import ROOT_DIR
from project import get_stats, project_metadata, analizeProject
from utils import display_project
from pprint import pprint


def init():
    projects_list = os.listdir(ROOT_DIR)
    projects = list()

    for project in projects_list:
        metadata = project_metadata(project)
        result = analizeProject(project)
        metadata['stack'] = result
        display_project(metadata)
        projects.append(metadata)
    
    get_stats(projects)


if __name__ == '__main__':
    init()