'''
Created on 25 mars 2015

@author: e_afauco
'''

import traceback

import stbx.path_tools
import stbx.date_tools

from core.internal_error import internal_error
from configuration_pckg.generic_ini_parser import generic_ini_parser
        

class parser_ini():
    
    def __init__(self, configuration_file):
        self.configuration_file = configuration_file
        self.generic_decoder    = generic_ini_parser(configuration_file)
        self.extensions_list    = []
        self.views_list         = []
    
    # Public method
    def proceed_decoding(self):
        
        # Get default section
        self.extensions_list = ''.join(self.generic_decoder.get_field('DEFAULT', 'EXTENSION').split()).split(';')
        
        # Get views
        sections_list = self.generic_decoder.get_sections_list()
        for section in sections_list:
            new_view = {'ID' : section}
            
            fields_list = ['FOLDER_PATH', 'TYPE', 'DATE', 'COMMENT']
            for field in fields_list:
                try:
                    new_view[field] = self.generic_decoder.get_field(section, field)
                except:
                    NewError = parser_ini_error(self, "field " + field + "' is not in section: " + section)
                    raise NewError
            
                # Validate fields
                new_view[field] = self.__validate_field(field, new_view[field])
            
            # Validate section
            if new_view['TYPE'] == 'backup' or new_view['TYPE'] == 'working':
                if new_view['DATE'] == '':
                    NewError = parser_ini_error(self, "In section: " + section + " - A view of type " + new_view['TYPE'] + " shall have a defined DATE field")
                    raise NewError
            
            # Append the decoded informations
            self.views_list.append(new_view)
            
    def get_extensions_list(self):
        return self.extensions_list
            
    def get_views_list(self):
        return self.views_list
        
    # Private method
    def __validate_field(self, field, value):
        if field == 'FOLDER_PATH':
            folder_path = value
            folder_path = stbx.path_tools.normalize_path(folder_path)
            if stbx.path_tools.does_folder_exist(folder_path) == False:
                NewError = parser_ini_error(self, "FOLDER_PATH: '" + str(folder_path) + "' is not valid")
                raise NewError
            return folder_path
            
        elif field == 'TYPE':
            _type = value
            if _type != 'versioned' and _type != 'backup' and _type != 'working':
                NewError = parser_ini_error(self, "TYPE: '" + str(_type) + "' is not valid")
                raise NewError
            return _type
        
        elif field == 'DATE':
            _date = value
            if _date != '':
                if stbx.date_tools.is_date_valid(_date) == False:
                    NewError = parser_ini_error(self, "DATE: '" + str(_date) + "' is not valid")
                    raise NewError
            return _date
        
        elif field == 'COMMENT':
            _comment = value
            return _comment
        
        else:
            NewError = internal_error(traceback.extract_stack())
            raise NewError





class parser_ini_error(parser_ini, Exception):
    def __init__(self, parent, message):
        self.message = "In " + parent.configuration_file + ": " + message