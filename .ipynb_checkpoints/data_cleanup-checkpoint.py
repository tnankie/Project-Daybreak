import time
import numpy as np
import os 
import pandas as pd
print(os.listdir(), '\n', os.getcwd())

with open('TADPOLE_D1_D2.csv', 'r') as init_data:
    raw_data = pd.read_csv(init_data)
# problem with mixed data, cols 471-831 (roughly)    
#%%     
# remove space characters from fields
p_data = raw_data.replace(to_replace = ' ', value = np.nan)
#fill by patient average wont have any effect on patients who never had a particular test

tic = time.perf_counter()
fill4 = p_data.fillna(p_data.groupby('RID').transform('mean'))
toc = time.perf_counter()
print(toc-tic)


#remove columns with less than 80% occupancy




p_data = fill4.loc[:, fill4.count() > len(fill4) * 0.8]

p_data['DX'] = fill4.loc[:,'DX']
p_data['DXCHANGE'] = fill4.loc[:,'DXCHANGE']
p_data['CDRSB'] = fill4['CDRSB']
p_data[['MMSE', 'RAVLT_immediate', 'Hippocampus', 'WholeBrain', 'Entorhinal', 
        'MidTemp', 'FDG', 'AV45', 'ABETA_UPENNBIOMK9_04_19_17', 'TAU_UPENNBIOMK9_04_19_17', 
        'PTAU_UPENNBIOMK9_04_19_17', 'APOE4', 'AGE']] = fill4[['MMSE', 'RAVLT_immediate', 
                                                     'Hippocampus', 'WholeBrain', 'Entorhinal', 
                                                     'MidTemp', 'FDG', 'AV45', 'ABETA_UPENNBIOMK9_04_19_17', 
                                                     'TAU_UPENNBIOMK9_04_19_17', 'PTAU_UPENNBIOMK9_04_19_17', 
                                                     'APOE4', 'AGE']]
clean_data = p_data.set_index('RID')
clean_data = clean_data.drop(['PTID', 'SITE', 'D1', 'D2', 'COLPROT', 'ORIGPROT'], axis=1)

#%%
print(clean_data.VISCODE.value_counts())
#1=Stable:NL to NL, 2=Stable:MCI to MCI, 3=Stable:AD to AD, 4=Conv:NL to MCI, 
#5=Conv:MCI to AD, 6=Conv:NL to AD, 7=Rev:MCI to NL, 8=Rev:AD to MCI, 
#9=Rev:AD to NL, -1=Not available
print(clean_data.DX_bl.value_counts())
print(clean_data.DX.value_counts())
print(clean_data.DXCHANGE.value_counts())
#%%
diags = clean_data[pd.notnull(clean_data.DX_bl) & (pd.notnull(clean_data.DX) | pd.notnull(clean_data.DXCHANGE))]
print('all records with BL diagnosis and either dx or dxchange')
print(diags.DX.value_counts())
print(diags.DX_bl.value_counts())
print(diags.DXCHANGE.value_counts())
print(diags.VISCODE.value_counts())
#%%
problems = clean_data.reset_index().merge(diags.reset_index(), how='outer', indicator=True).loc[lambda x : x['_merge']=='left_only']
print(problems.VISCODE.value_counts())
print(problems.DX.value_counts())
print(problems.DX_bl.value_counts())
print(problems.DXCHANGE.value_counts())
print(problems.head())
#%%
prob_bl_RID = problems[['RID', 'DX', 'DX_bl', 'DXCHANGE']][problems.VISCODE == 'bl']
test_list = clean_data.reset_index().iloc[0:10,0]
test_list2 = [2,3,4,5]
test_bl_RID_full = clean_data.reset_index()[['RID', 'DX', 'DX_bl', 'DXCHANGE','VISCODE']][clean_data.reset_index().RID.isin(test_list)]
test_bl_RID_full2 = clean_data.reset_index()[['RID', 'DX', 'DX_bl', 'DXCHANGE','VISCODE']][clean_data.reset_index().RID.isin(test_list2)]
prob_bl_RID_full = clean_data.reset_index()[['RID', 'DX', 'DX_bl', 'DXCHANGE','VISCODE']][clean_data.reset_index().RID.isin(prob_bl_RID.RID)]
print('-----------------------------------\nExample problems, transitional patient RID:2 that reverts but never records the reversion')
print(test_bl_RID_full.set_index('RID').sort_index())

#%%
vis_codes = clean_data.VISCODE.unique()
vis_nums = []
for x in vis_codes:
    if x == 'bl':
        vis_nums.append(0)
    else:
        vis_nums.append(int(x[1:]))
        
clean_data['VISNUMS'] = clean_data.VISCODE
clean_data.VISNUMS = clean_data.VISNUMS.replace(to_replace=vis_codes , value=vis_nums)
clean_data2 = clean_data.reset_index().set_index(['RID','VISNUMS']).sort_index()
print(clean_data2.loc[2,['DX', 'DX_bl', 'DXCHANGE']])
print(clean_data2.loc[prob_bl_RID.RID,['DX', 'DX_bl', 'DXCHANGE']])

#%%
#dropping the DX_bl odd cases
#clean_data3 = clean_data[clean_data[~((clean_data.VISCODE == 0) & (clean_data.DX_bl == 'EMCI') & pd.isnull(clean_data.DX) & pd.isnull(clean_data.DXCHANGE))]] 
#%%
w_data = clean_data.reset_index()
w_data = w_data.sort_values(['RID', 'VISNUMS'])
w_data = w_data.drop(['FLDSTRENG_bl', 'FSVERSION_bl', 'update_stamp'], axis = 1)

#dummy variables for marital status
w_test = pd.get_dummies(w_data.PTMARRY, prefix ='m_stat')
#w_data = pd.concat([w_data, w_test], axis=1)
#w_data = w_data.drop(['PTMARRY'], axis=1)

#dummy varriables for gender
w_test = pd.get_dummies(w_data.PTGENDER)
#w_data = pd.concat([w_data, w_test], axis=1)
#w_data = w_data.drop(['PTGENDER'], axis=1)

#dummy variables for ethnicity
w_test = pd.get_dummies(w_data.PTETHCAT, prefix='ethnicity')
#w_data = pd.concat([w_data, w_test], axis=1)
#w_data = w_data.drop(['PTETHCAT'], axis=1)

#dummy variables for race
w_test = pd.get_dummies(w_data.PTRACCAT, prefix='race')
#w_data = pd.concat([w_data, w_test], axis=1)
#w_data = w_data.drop(['PTRACCAT'], axis=1)

#%%
#more data cleaning
w_data = w_data.drop(['VISCODE'], axis=1)
w_data.ABETA_UPENNBIOMK9_04_19_17 = w_data.ABETA_UPENNBIOMK9_04_19_17.str.strip()
test = w_data.ABETA_UPENNBIOMK9_04_19_17.str.startswith('<')
test = test.fillna(value=False)

#as a result of data exploration found one instance of ABETA_UPENNBIOMK9_04_19_17 <200
# to address this problem this value was set to 100
w_data.loc[w_data[test].index.values,'ABETA_UPENNBIOMK9_04_19_17'] = 100
w_data.ABETA_UPENNBIOMK9_04_19_17 = pd.to_numeric(w_data.ABETA_UPENNBIOMK9_04_19_17)

#as a result of data exploration found 8 instances of TAU_UPENNBIOMK9_04_19_17 <80
#to address this issue setting these to value of 40
w_data.TAU_UPENNBIOMK9_04_19_17 = w_data.TAU_UPENNBIOMK9_04_19_17.str.strip()
test = w_data.TAU_UPENNBIOMK9_04_19_17.str.startswith('<')
test = test.fillna(value=False)
w_data.loc[w_data[test].index.values,'TAU_UPENNBIOMK9_04_19_17'] = 40

#further data exploration revealed values of TAU_UPENNBIOMK9_04_19_17 >1300
#these values have been set to 1500
test = w_data.TAU_UPENNBIOMK9_04_19_17.str.startswith('>')
test = test.fillna(value=False)
w_data.loc[w_data[test].index.values,'TAU_UPENNBIOMK9_04_19_17'] = 1500

w_data.TAU_UPENNBIOMK9_04_19_17 = pd.to_numeric(w_data.TAU_UPENNBIOMK9_04_19_17)

w_data.PTAU_UPENNBIOMK9_04_19_17 = w_data.PTAU_UPENNBIOMK9_04_19_17.str.strip()

#some values of PTAU_UPENNBIOMK9_04_19_17 >120 were found
#these have been set to 150
test = w_data.PTAU_UPENNBIOMK9_04_19_17.str.startswith('>')
test = test.fillna(value=False)
w_data.loc[w_data[test].index.values,'PTAU_UPENNBIOMK9_04_19_17'] = 150

#some values of PTAU_UPENNBIOMK9_04_19_17 <8 were found
#these have been set to 4
test = w_data.PTAU_UPENNBIOMK9_04_19_17.str.startswith('<')
test = test.fillna(value=False)
w_data.loc[w_data[test].index.values,'PTAU_UPENNBIOMK9_04_19_17'] = 4

w_data.PTAU_UPENNBIOMK9_04_19_17 = pd.to_numeric(w_data.PTAU_UPENNBIOMK9_04_19_17)
w_data.to_csv('plot_time_2.csv')
print(w_data.loc[w_data.RID==2,:])
print('done')