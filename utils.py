from constants import DEFAULT_FILES
import os 

def is_default_file(file):
    return file in DEFAULT_FILES

def get_file_type(file):
    file_extension = file.split('.')[-1]
    return file_extension.upper()
