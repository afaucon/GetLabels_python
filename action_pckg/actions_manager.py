'''
Created on 26 mars 2015

@author: e_afauco
'''

import traceback

from stbx.path_tools import does_folder_exist
from stbx.date_tools import is_date_valid

from core.internal_error import internal_error

from action_pckg.displayable_list import displayable_list



def action_add_a_view_from_disk(view_path, view_type, view_date, view_comment):
    pass
    
def action_remove_a_view(view_ID, shall_be_deleted_from_disk):
    pass

def action_show_view_information(view_ID):
    pass

def action_duplicate_a_view_and_old_attributes(from_view_ID, to_view_path):
    pass

def action_duplicate_a_view_and_new_attributes(from_view_ID, to_view_path):
    pass

def action_compare_two_views(left_view_ID, right_view_ID, subfolder_path):
    pass

    
    
    
    
    
    
    
class actions_manager():
    def __init__(self, conf_mgr, views_mgr):
        self.conf_mgr    = conf_mgr
        self.views_mgr   = views_mgr
        
        self.view_objects_list = self.views_mgr.get_views_objects_list_to_actions_manager()
        
        self.argument_types_list = self.conf_mgr.get_argument_types_list_for_actions_manager()
        self.actions_list        = self.conf_mgr.get_actions_list_for_action()
        
        self.user_invalid_argument_info = {'state' : 'is valid argument shall be called',
                                           'reason': ''}
    
    def get_argument_range_info(self, argument_type):        
        if argument_type == 'PATH':
            new_range = displayable_list("The path shall exist", 1)
        elif argument_type == 'VIEW_TYPE':
            new_range = displayable_list("The view type shall be chosen from the list", 1)
            new_range.add_item(["versionned"])
            new_range.add_item(["working"])
            new_range.add_item(["backup"])
        elif argument_type == 'VIEW_DATE':
            new_range = displayable_list("The date shall be in the form yyyy-mm-dd", 1)
        elif argument_type == 'VIEW_COMMENT':
            new_range = displayable_list("Any texts is accepted as comment", 1)
        elif argument_type == 'VIEW_ID':
            new_range = displayable_list("The view type shall be chosen from the list", 1)
            item = []
            for view_object in self.view_objects_list:
                view_object_content = view_object.get_view_content()
                new_range.add_item(item)
        elif argument_type == 'VIEW_SHALL_BE_DELETED_FROM_DISK':
            new_range = displayable_list("The only valid values for this field are one of those", 2)
            new_range.add_item(["yes", "The view will be deleted from disk"])
            new_range.add_item(["no",  "The view will stay on the disk"])
        else:
            NewError = internal_error(traceback.extract_stack())
            raise NewError
        return new_range
    
    ####################################################################
    # Dataflow to display_manager
    ####################################################################
    
    def get_actions_descriptions_list_to_display_manager(self):
        action_descriptions_list = []
        for action in self.actions_list:
            action_descriptions_list.append(action.get_description())
        return action_descriptions_list
    
    def get_action_arguments_descriptions_and_range_info_list_to_display_manager(self, action_position):
        action = self.actions_list[action_position]        
        action_arguments_descriptions_and_range_info_list = []
        for argument in action.get_arguments_list(): 
            new_info = {'description': argument.get_description(),
                        'range info' : self.get_argument_range_info(argument.get_type())} 
            action_arguments_descriptions_and_range_info_list.append(new_info)
        return action_arguments_descriptions_and_range_info_list
    
    ####################################################################
    # Dataflow from display_manager
    ####################################################################
        
    def action_argument_value_is_valid_from_display_manager(self, action_position, action_argument_position, action_argument_value):
        action         = self.actions_list[action_position]
        argument       = action.get_arguments_list()[action_argument_position]
        argument_type  = argument.get_type()
        argument_value = action_argument_value 

        if self.user_invalid_argument_info['state'] == 'is valid argument shall be called':
            
            if argument_type == 'PATH':
                if does_folder_exist(argument_value) == False:
                    self.user_invalid_argument_info = {'state':'why invalid argument shall be called', 'reason':self.get_argument_range_info(argument_type)['information']}
                    return False
                return True
            elif argument_type == 'VIEW_TYPE':
                if argument_value != 'versioned' and argument_value != 'backup' and argument_value != 'working':
                    self.user_invalid_argument_info = {'state':'why invalid argument shall be called', 'reason':self.get_argument_range_info(argument_type)['information']}
                    return False
                return True
            elif argument_type == 'VIEW_DATE':
                if is_date_valid(argument_value) == False:
                    self.user_invalid_argument_info = {'state':'why invalid argument shall be called', 'reason':self.get_argument_range_info(argument_type)['information']}
                    return False
                return True
            elif argument_type == 'VIEW_COMMENT':
                return True
            elif argument_type == 'VIEW_ID':
                if self.views_mgr.view_id_is_valid_to_actions_manager(argument_value) == False:
                    self.user_invalid_argument_info = {'state':'why invalid argument shall be called', 'reason':self.get_argument_range_info(argument_type)['information']}
                    return False
                return True
            elif argument_type == 'VIEW_SHALL_BE_DELETED_FROM_DISK':
                if argument_value != 'no' and argument_value != 'yes':
                    self.user_invalid_argument_info = {'state':'why invalid argument shall be called', 'reason':self.get_argument_range_info(argument_type)['information']}
                    return False
                return True
            else:
                NewError = internal_error(traceback.extract_stack())
                raise NewError
        else:
            NewError = internal_error(traceback.extract_stack())
            raise NewError
    
    def why_argument_value_is_invalid_from_display_manager(self):
        if self.user_invalid_argument_info['state'] == 'why invalid argument shall be called':
            self.user_invalid_argument_info['state'] = 'is valid argument shall be called'
            return self.user_invalid_argument_info['reason']
        else:
            NewError = internal_error(traceback.extract_stack())
            raise NewError
        
    def launch_action_from_display_manager(self, action_name, arguments_values_list):
        if action_name == 'ADD_VIEW_FROM_DISK':
            action_add_a_view_from_disk(arguments_values_list[0], arguments_values_list[1], arguments_values_list[2], arguments_values_list[3])
        elif action_name == 'REMOVE_A_VIEW':
            action_remove_a_view(arguments_values_list[0], arguments_values_list[1])
        elif action_name == 'SHOW_VIEW_INFO':
            action_show_view_information(arguments_values_list[0])
        elif action_name == 'DUPLICATE_VIEW_KEEP_OLD_ATTR':
            action_duplicate_a_view_and_old_attributes(arguments_values_list[0], arguments_values_list[1])
        elif action_name == 'DUPLICATE_VIEW_SET_NEW_ATTR':
            action_duplicate_a_view_and_new_attributes(arguments_values_list[0], arguments_values_list[1])
        elif action_name == 'COMPARE_2_VIEWS':
            action_compare_two_views(arguments_values_list[0], arguments_values_list[1], arguments_values_list[2])
        else:
            NewError = internal_error(traceback.extract_stack())
            raise NewError


