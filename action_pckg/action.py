'''
Created on 1 avr. 2015

@author: e_afauco
'''


class argument():
    def __init__(self, type, description):
        self.type        = type
        self.description = description
    
    def get_type(self):
        return self.type
    
    def get_description(self):
        return self.description
        
        
class action():
    def __init__(self, name, description):
        self.name           = name
        self.description    = description
        self.arguments_list = [] 
        
    def add_new_argument(self, type, description):
        new_argument = argument(type, description)
        self.arguments_list.append(new_argument)
    
    def get_description(self):
        return self.description
        
    def get_arguments_list(self):
        return self.arguments_list