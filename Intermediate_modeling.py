# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:17:00 2019

@author: Grey Ghost
"""


import numpy as np
import seaborn as sns
import os 
import pandas as pd
import sklearn as sk
from sklearn import svm
import matplotlib.pyplot as plt
print(os.listdir(), '\n', os.getcwd())

with open('90percent_data.csv', 'r') as init_data:
    raw_data = pd.read_csv(init_data, index_col='RID')
#%%
raw_data = raw_data.iloc[:,1:]
raw_data = raw_data.drop(['PTID','SITE', 'D1', 'D2', 'COLPROT', 'ORIGPROT','FSVERSION_bl'], axis=1)
gender_list = raw_data.loc[:,'PTGENDER'].unique()
gender_vals = []
for i in range(len(gender_list)):
    gender_vals.append(i)
DX_list = raw_data.loc[:,'DX_bl'].unique()
DX_vals = []
for i in range(len(DX_list)):
    DX_vals.append(i)

raw_data = raw_data.replace(to_replace = DX_list, value=DX_vals)
raw_data = raw_data.replace(to_replace = gender_list, value=gender_vals)
raw_data['VISCODE'] = raw_data['VISCODE'].astype('category')



print(raw_data.info())