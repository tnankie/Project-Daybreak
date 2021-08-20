# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:44:42 2019

@author: Grey_Ghost
"""

import numpy as np
import seaborn as sns
import os 
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
print(os.listdir(), '\n', os.getcwd())

with open('TADPOLE_D1_D2.csv', 'r') as init_data:
    raw_data = pd.read_csv(init_data)
    
#%%     
def str2fl(s):
    #if the input type is a string and can be converted to a float it does so, otherwise returns the unmodified string
    if s == ' ':
        s = ''
        
    if type(s) == str:
       try:
           n = float(s)
       except:
           n = s
    else:
        n = s
    return(n)
    
print(raw_data.shape)
rraw_data = raw_data.loc[:,raw_data.count() > len(raw_data) * 0.9]
print(rraw_data.shape)
# remove space characters from fields
p_data = rraw_data.replace(to_replace = ' ', value = None)
#remove columns with less than 90% occupancy
p_data = p_data.loc[:, p_data.count() > len(p_data) * 0.9]
print(p_data.shape)
pp_data = p_data.applymap(str2fl)
pp_data = pp_data.dropna()
print(pp_data.info(), pp_data.shape)
