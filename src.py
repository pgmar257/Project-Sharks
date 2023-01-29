#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import numpy as np
import regex as re
from datetime import date, datetime, timedelta 
import requests 
import seaborn as sns


def fecha_limpia(x):
    try:
        if re.match('[0-9]{2}-[a-zA-Z]{3}--[0-9]{4}',x):
            return datetime.strptime(x,"%d-%b--%Y").date()
        elif re.match('[a-zA-Z]{3}-[0-9]{4}',x):
            return datetime.strptime(x, "%b-%Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}[0-9]{4}',x):
            return datetime.strptime(x,"%d-%b%Y").date()
        elif re.match('[a-zA-Z]{3} [0-9]{4}',x):
            return datetime.strptime(x, "%b %Y").date()
        elif re.match('[a-zA-Z]{3}[0-9]{4}',x):
            return datetime.strptime(x, "%b%Y").date()
        elif re.match('\s[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}',x):
            return datetime.strptime(x," %d-%b-%Y").date()
        elif re.match('[0-9]{4}$',x):
            return datetime.strptime(x,"%Y").date()
        elif re.match('[a-zA-Z]+ [0-9]{4}',x):
            return datetime.strptime(x, "%B %Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}.+',x):
            return datetime.strptime(x.split('.')[0],"%d-%b-%Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}.+',x):
            return datetime.strptime(x,"%d-%b-%Y ").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}', x):
            return datetime.strptime(x,"%d-%b-%Y").date()   
        elif 'or' in x:
            return datetime.strptime(x.split('or')[0],"%d-%b-%Y").date()
                                     
        else : 
            x = '01-01-1000'
            return datetime.strptime(x,"%d-%m-%Y").date()
        
        
    except ValueError as e:
        x = '01-01-1000'
        return datetime.strptime(x,"%d-%m-%Y").date()
        pass
    
def fecha_limpia2():

    try:
        if re.match('[0-9]{2}-[a-zA-Z]{3}--[0-9]{4}',x):
            return datetime.strptime(x,"%d-%b--%Y").date()
        elif re.match('[a-zA-Z]{3}-[0-9]{4}',x):
            return datetime.strptime(x, "%b-%Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}[0-9]{4}',x):
            return datetime.strptime(x,"%d-%b%Y").date()
        elif re.match('[a-zA-Z]{3} [0-9]{4}',x):
            return datetime.strptime(x, "%b %Y").date()
        elif re.match('[a-zA-Z]{3}[0-9]{4}',x):
            return datetime.strptime(x, "%b%Y").date()
        elif re.match('\s[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}',x):
            return datetime.strptime(x," %d-%b-%Y").date()
        elif re.match('[0-9]{4}$',x):
            return datetime.strptime(x,"%Y").date()
        elif re.match('[a-zA-Z]+ [0-9]{4}',x):
            return datetime.strptime(x, "%B %Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}.+',x):
            return datetime.strptime(x.split('.')[0],"%d-%b-%Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}.+',x):
            return datetime.strptime(x,"%d-%b-%Y ").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}', x):
            return datetime.strptime(x,"%d-%b-%Y").date()   
        elif 'or' in x:
            return datetime.strptime(x.split('or')[0],"%d-%b-%Y").date()
                                     
        else : 
            x = '01-01-1000'
            return datetime.strptime(x,"%d-%m-%Y").date()

    except ValueError as e:
        x = '01-01-1000'
        return datetime.strptime(x,"%d-%m-%Y").date()
        pass

    
def value_to_num(x):
    if type(x) == int:
        return x
    elif type(x) == float:
        return  x
    else:
        re.sub('[^0-9]', '', x)
        if re.match('[0-9]+',x):
            x =  x [0:2]
        return x    