'''
Created on 24 mars 2015

@author: e_afauco
'''

from configparser import ConfigParser


class generic_ini_parser():
        
    def __init__(self, configuration_file):
        self.configuration_file = configuration_file
        
        # Read the configuration file
        self.parser = ConfigParser()
        self.parser.read(configuration_file)

    def get_configuration_file(self):
        return self.configuration_file
    
    def get_sections_list(self):
        return self.parser.sections()
    
    def get_field(self, section, field):
        return self.parser[section][field]