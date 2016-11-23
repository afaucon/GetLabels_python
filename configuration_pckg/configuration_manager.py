'''
Created on 31 mars 2015

@author: e_afauco
'''

import sys

from configuration_pckg.parser_ini import parser_ini
from configuration_pckg.parser_ini import parser_ini_error
from configuration_pckg.parser_xml import parser_xml
from configuration_pckg.parser_xml import parser_xml_error


class configuration_manager():
    def __init__(self, user_ini_file, action_xml_file):
        
        self.user_ini_file   = user_ini_file
        self.action_xml_file = action_xml_file
                
        try:
            self.parser_ini = parser_ini(user_ini_file)
        except parser_ini_error as e:
            print(e.message)
            sys.exit(0)
        
        try:
            self.parser_xml = parser_xml(action_xml_file)
        except parser_xml_error as e:
            print(e.message)
            sys.exit(0)
            
    def proceed_decoding(self):
        try:
            self.parser_ini.proceed_decoding()
        except parser_ini_error as e:
            print(e.message)
            sys.exit(0)
            
    #######################################################################
    # Dataflow to views_manager        
    #######################################################################
    
    def get_views_list_to_views_manager(self):
        return self.parser_ini.get_views_list()
    
    #######################################################################
    # Dataflow to actions_manager
    #######################################################################
    
    def get_argument_types_list_for_actions_manager(self):
        return self.parser_xml.get_argument_types_list()
    
    def get_actions_list_for_action(self):
        return self.parser_xml.get_actions_list()