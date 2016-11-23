'''
Created on 23 mars 2015

@author: e_afauco
'''

import os 

LANGUAGE_VERSION_LOCATION_C    = "./sigertms/language_tools/code_and_test/common_language/src/language_version.ads"
APPLICATION_VERSION_LOCATION_C = "./sigertms/trainborne/products/evc/core/sw/appli_sw/code_and_test/src/app_interface/evc_version.ads"

class view_error(Exception):
    def __init__(self, view, message):
        self.message = "In view " + view.get_root_path() + ": " + message


class view:
    def __init__(self, ID, root_path, atype, date, comment):
        self.ID = ID
        self.root_path = root_path
        self.type = atype
        self.date = date
        self.comment = comment
        self.SRDVersion = self.PerformDeepAnalizisToGetSRDVersion()
        self.LanguageLabel = self.PerformDeepAnalizisToGetLanguageLabel()
        self.ApplicationLabel = self.PerformDeepAnalizisToGetApplicationLabel()
    
    ##################################################################################################################################
    # Private methods
    ##################################################################################################################################
    def Search(self, root_path, file, pattern):
        os.chdir(root_path)
        try:
            searchfile = open(file, "r")
        except:
            NewError = view_error(self, "Cannot open file " + str(file))
            raise NewError
            
        for line in searchfile:
            if pattern in line:
                searchfile.close()
                return line
            
        searchfile.close()
        return ""

    def PerformDeepAnalizisToGetSRDVersion(self):
        return self.Search(self.root_path, APPLICATION_VERSION_LOCATION_C, 'SRD').split(':=')[1].split('"')[1]
    
    def PerformDeepAnalizisToGetLanguageLabel(self):
        return self.Search(self.root_path, LANGUAGE_VERSION_LOCATION_C, 'LABEL').split(':=')[1].split('"')[1]
    
    def PerformDeepAnalizisToGetApplicationLabel(self):
        return self.Search(self.root_path, APPLICATION_VERSION_LOCATION_C, 'LABEL').split(':=')[1].split('"')[1]
    
    ##################################################################################################################################
    # Public interface
    ##################################################################################################################################
    def get_id(self):
        return self.ID
    
    def get_view_content(self):
        view = {'id'              : {'value': self.ID,               'description': "ID"},
                'root_path'       : {'value': self.root_path,        'description': "Path"},
                'type'            : {'value': self.type,             'description': "Type"},
                'date'            : {'value': self.date,             'description': "Date"},
                'comment'         : {'value': self.comment,          'description': "Comment"},
                'SRDVersion'      : {'value': self.SRDVersion,       'description': "SRD Version"},
                'LanguageLabel'   : {'value': self.LanguageLabel,    'description': "Clearcase label for the language"},
                'ApplicationLabel': {'value': self.ApplicationLabel, 'description': "Clearcase label for the application"}
                }
        return view

    def print_view_repport(self):
        print("Id                : " + self.ID)
        print("Root path         : " + self.root_path)
        print("SRD version       : " + self.SRDVersion)
        print("Language label    : " + self.LanguageLabel)
        print("Application label : " + self.ApplicationLabel)