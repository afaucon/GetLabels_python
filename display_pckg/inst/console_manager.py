'''
Created on 27 mars 2015

@author: e_afauco
'''

from display_pckg.display_manager import display_manager
from display_pckg.display_manager import display_manager_error
    



class console_manager(display_manager):
    
    def __init__(self, action_mgr):
        self.action_mgr = action_mgr
    
    def run(self):
        while(1):
            actions_descriptions_list = self.action_mgr.get_actions_descriptions_list_to_display_manager()
            minVal = 0
            maxVal = len(actions_descriptions_list) -1
            
            print("----------------------------------------")
            print("Choose an action by entering a action number from " + str(minVal) + " to " + str(maxVal) + ".")
            
            for action_description in actions_descriptions_list:
                print("[" + str(actions_descriptions_list.index(action_description)) + "] " + action_description)
            
            while(True):
                print(">> ", end=" ")
                ans = input()
                try:
                    action_position = int(ans)
                    if action_position < minVal or action_position > maxVal:
                        raise ValueError
                    break
                except ValueError:
                    print("Error: You must enter a valid number.")
                    
            action_arguments_descriptions_and_range_info_list = self.action_mgr.get_action_arguments_descriptions_and_range_info_list_to_display_manager(action_position)
            
            for action_argument_description_and_range_info in action_arguments_descriptions_and_range_info_list:
                action_argument_position = action_arguments_descriptions_and_range_info_list.index(action_argument_description_and_range_info)
                
                while(True):
                    print(action_argument_description_and_range_info['description'])
                    print(action_argument_description_and_range_info['range info']['information']) 
                    for possible_value in action_argument_description_and_range_info['range info']['range']:
                        print(' - "' + possible_value + '"')
                    print('>> ', end=" ")
                    action_argument_value = input()
                    if self.action_mgr.action_argument_value_is_valid_from_display_manager(action_position, action_argument_position, action_argument_value) == True:
                        break
                    else:
                        print("Invalid entry:")
                        print(self.action_mgr.why_argument_value_is_invalid_from_display_manager())
                        print()
            
            # self.action_mgr.launch_action_from_display_manager(action_name, arguments_values_list)
            
            
            
    
class console_manager_error(Exception, display_manager):
    def __init__(self, message):
        display_manager_error.__init__(self, message)