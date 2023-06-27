# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:03:39 2022

@author: yuxue
"""

import os
import pandas as pd 
from minepy import MINE
import numpy as np
 
inpath = os.getcwd()+'/prediction_all.csv'
dataset = pd.read_csv(inpath, header=0, encoding='gbk')
values = dataset.values
# ensure all data is float
fdata = values.astype('float64')
x=fdata[:,0:-1]   
data_y=fdata[:,-1]
outpath =os.getcwd()+'/MIC系数.csv' 
depend_names=[]
value_mic=[] 
output_mic = pd.DataFrame(columns=['变量1','变量2','MIC系数'])
k=0
print(len(x[0,:]))
for var1 in range(len(x[0,:])):
    if k==19:
        k=0
    depend_names.append('变量'+str(18-k))  
    data_x=x[:,var1]
    mine = MINE(alpha = 0.6, c = 15)
    mine.compute_score(data_x, data_y)
    mine = MINE(alpha = 0.6, c = 15)
    mine.compute_score(data_x, data_y)  
#    print(mine.mic())
    value_mic.append(mine.mic()) 
    k=k+1
output_mic1 = pd.DataFrame(value_mic, columns=['MIC系数'])
output_mic2 = pd.DataFrame(depend_names, columns=['变量'])
output_mic = pd.DataFrame(
    pd.concat(
        [   output_mic2,
            output_mic1,
        ],
        axis=1))
output_mic.to_csv(outpath)


inpath = os.getcwd()+'/prediction_all_c1.csv'
dataset = pd.read_csv(inpath, header=0, encoding='gbk')
values = dataset.values
# ensure all data is float
fdata = values.astype('float64')
x=fdata[:,0:-1]   
data_y=fdata[:,-1]
outpath =os.getcwd()+'/MIC系数_c1.csv' 
depend_names=[]
value_mic=[] 
output_mic = pd.DataFrame(columns=['变量1','变量2','MIC系数'])
k=0
for var1 in range(len(x[0,:])):
    if k==19:
        k=0
    depend_names.append("变量"+str(18-k)) 
    data_x=x[:,var1]
    mine = MINE(alpha = 0.6, c = 15)
    mine.compute_score(data_x, data_y)
    mine = MINE(alpha = 0.6, c = 15)
    mine.compute_score(data_x, data_y)  
#    print(mine.mic())
    value_mic.append(mine.mic())    
    k=k+1
output_mic1 = pd.DataFrame(value_mic, columns=['MIC系数'])
output_mic2 = pd.DataFrame(depend_names, columns=['变量'])
output_mic = pd.DataFrame(
    pd.concat(
        [   output_mic2,
            output_mic1,
        ],
        axis=1))
output_mic.to_csv(outpath)

inpath = os.getcwd()+'/prediction_all_c2.csv'
dataset = pd.read_csv(inpath, header=0, encoding='gbk')
values = dataset.values
# ensure all data is float
fdata = values.astype('float64')
x=fdata[:,0:-1]   
data_y=fdata[:,-1]
outpath =os.getcwd()+'/MIC系数_c2.csv' 
depend_names=[]
value_mic=[] 
output_mic = pd.DataFrame(columns=['变量1','变量2','MIC系数'])
k=0
for var1 in range(len(x[0,:])):
    if k==19:
        k=0
    depend_names.append("变量"+str(18-k)) 
    data_x=x[:,var1]
    mine = MINE(alpha = 0.6, c = 15)
    mine.compute_score(data_x, data_y)
    mine = MINE(alpha = 0.6, c = 15)
    mine.compute_score(data_x, data_y)  
#    print(mine.mic())
    value_mic.append(mine.mic())    
    k=k+1
output_mic1 = pd.DataFrame(value_mic, columns=['MIC系数'])
output_mic2 = pd.DataFrame(depend_names, columns=['变量'])
output_mic = pd.DataFrame(
    pd.concat(
        [   output_mic2,
            output_mic1,
        ],
        axis=1))
output_mic.to_csv(outpath)