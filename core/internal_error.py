'''
Created on 25 mars 2015

@author: e_afauco
'''

class internal_error(Exception):
    def __init__(self, stack):
        filename, codeline, funcName, text = stack[-2]
        message = "Internal error in:\n" + \
                   "File: " + filename + "\n" + \
                   "Line number: " + str(codeline) + "\n" + \
                   "Function: " + funcName + "\n" + \
                   "Line: " + text
        self.message = message