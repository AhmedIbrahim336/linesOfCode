from constants import DEFAULT_FILES, bcolors


def is_default_file(file):
    return file in DEFAULT_FILES

def get_file_type(file):
    file_extension = file.split('.')[-1]
    return file_extension.upper()

def cprint(text, mode = None):
    print(f"{bcolors.BOLD}{text}{bcolors.ENDC}")

def display_project(metadata):
    # Todo: all of these values are optional so need to be validated
    tags = ', '.join((metadata['tags']))
    stacks = ', '.join(metadata.get('stack', {}).keys())
    print(f"{bcolors.HEADER}Name: {metadata['name']}{bcolors.ENDC}")
    print(f"{bcolors.BOLD}Description: {metadata['description']}{bcolors.ENDC}")
    print(f"{bcolors.BOLD}Name: {tags}{bcolors.ENDC}")
    print(f"{bcolors.BOLD}Tech Stack: {stacks} {bcolors.ENDC}")
    for tech, lines in metadata.get('stack', {}).items():
        print(f"     {bcolors.BOLD}{tech}: {lines} line(s) {bcolors.ENDC}")
    print('\n')

def display_projects(projects):
    for project in projects:
        display_project(project)