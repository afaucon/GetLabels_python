'''
Created on 31 mars 2015

@author: e_afauco
'''

import datetime


def get_today_date():
    # Create the date string
    year_str  = "{0:04d}".format(datetime.datetime.today().year)
    month_str = "{0:02d}".format(datetime.datetime.today().month)
    day_str   = "{0:02d}".format(datetime.datetime.today().day)
    
    date_str = year_str + '-' + month_str + '-' + day_str
    
    return date_str

def is_date_valid(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False