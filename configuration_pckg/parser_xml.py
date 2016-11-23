'''
Created on 31 mars 2015

@author: e_afauco
'''

import xml.etree.ElementTree as ET

from action_pckg.action import action


class parser_xml():
    def __init__(self, configuration_file):
        self.configuration_file = configuration_file
        self.tree = ET.parse(configuration_file)
        self.root = self.tree.getroot()
    
    def get_argument_types_list(self):
        argument_types_list = []
        for child in self.root.findall("./argument_types/argument_type"):
            argument_types_list.append(child.attrib)
        return argument_types_list
    
    def get_actions_list(self):
        actions_list = []
        for child in self.root.findall("./actions/action"):
            new_action = action(child.attrib['name'], 
                                child.attrib['description'])

            for argument_type in child:
                new_action.add_new_argument(argument_type.attrib['type'],
                                            argument_type.attrib['description'])
            
            actions_list.append(new_action)
        return actions_list
     

    
class parser_xml_error(parser_xml, Exception):
    def __init__(self, parent, message):
        self.message = "In " + parent.configuration_file + ": " + message