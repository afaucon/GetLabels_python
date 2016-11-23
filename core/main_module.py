'''
Created on 23 mars 2015

@author: e_afauco
'''

import sys
import traceback

from configuration_pckg.configuration_manager import configuration_manager

from view_pckg.views_manager import views_manager
from view_pckg.views_manager import views_manager_error

from action_pckg.actions_manager import actions_manager

from display_pckg.inst.gui_manager     import gui_manager
from display_pckg.inst.cmdline_manager import cmdline_manager
from display_pckg.inst.console_manager import console_manager
from display_pckg.display_manager      import display_manager_error

from core.internal_error import internal_error


def main_procedure():
    
    conf_mgr = configuration_manager('config.ini', 'actions.xml')
    conf_mgr.proceed_decoding()
    
    try:
        views_mgr = views_manager(conf_mgr)
    except views_manager_error as e:
        print(e.message)
        sys.exit(0)
        
    action_mgr = actions_manager(conf_mgr, views_mgr)
        
    try:
        kind_of_display = 'console_mode'
        
        if kind_of_display == 'gui_mode':
            display_mgr = gui_manager(action_mgr)
            display_mgr.run()
        elif kind_of_display == 'cmdline_mode':
            display_mgr = cmdline_manager(action_mgr)
            display_mgr.run()
        elif kind_of_display == 'console_mode':
            display_mgr = console_manager(action_mgr)
            display_mgr.run()
        else:
            NewError = internal_error(traceback.extract_stack())
            raise NewError
        
    except display_manager_error as e:
        print(e.message)
        sys.exit(0)


if __name__ == '__main__':
    try:
        main_procedure()
    except internal_error as e:
        print(e.message)
        sys.exit(0)