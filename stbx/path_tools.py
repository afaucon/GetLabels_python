'''
Created on 27 mars 2015

@author: e_afauco
'''

import os


def normalize_path(path):
    path = os.path.normcase(path)
    path = os.path.normpath(path)
    path = os.path.realpath(path)
    return path

def does_folder_exist(folder_path):
    normalize_path(folder_path)
    if not os.access(folder_path, os.W_OK):
        return False
    return True
    