'''
Created on 25 mars 2015

@author: e_afauco
'''

import sys

from view_pckg.view import view
from view_pckg.view import view_error


class views_manager():    
    def __init__(self, conf_mgr):
        self.conf_mgr          = conf_mgr
        self.view_objects_list = []
        for one_view in conf_mgr.get_views_list_to_views_manager():
            try:
                new_view = view(one_view['ID'],
                                one_view['FOLDER_PATH'],
                                one_view['TYPE'],
                                one_view['DATE'],
                                one_view['COMMENT'])
            except view_error as e:
                print(e.message)
                sys.exit(0)
            
            self.view_objects_list.append(new_view)
    
    ##################################################################################################################################
    # Public interface
    ##################################################################################################################################
            
    def view_id_is_valid_to_actions_manager(self, view_id):
        for view_object in self.view_objects_list:
            if view_object.get_id() == view_id:
                return True
        return False
    
    def get_views_objects_list_to_actions_manager(self):
        return self.view_objects_list




class views_manager_error(views_manager, Exception):
    def __init__(self, message):
        # todo
        self.message = "Not yet implemented + " + message