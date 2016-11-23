'''
Created on 26 mars 2015

@author: e_afauco
'''

from display_pckg.display_manager import display_manager


class gui_manager(display_manager):
    def __init__(self, action_mgr):
        self.action_mgr = action_mgr