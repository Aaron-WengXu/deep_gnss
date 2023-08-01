import pandas as pd
import numpy as np
import os

# # 2021-04-22-SJC-1
# file_name = "2021-04-22-US-SJC-1"
# time0 = 1.303162070446000e+09
# timeE = 1.303162220446000e+09

# # 2021-04-29-SJC-2
# file_name = "2021-04-29-US-SJC-2"
# time0 = 1.303759020435000e+09
# timeE = 1.303759310435000e+09

# # 2021-04-28-SJC-1
# file_name = "2021-04-28-US-SJC-1"
# time0 = 1.303676058438000e+09
# timeE = 1.303676208438000e+09

# 2021-04-28-SJC-1 Generation Test
file_name = "2021-04-28-US-SJC-1"
time0 = 1.303676673438000e+09
timeE = 1.303676758438000e+09

# Read raw data
raw_data_dir = "RouteUS4O_G/"+file_name+"/Pixel4/Pixel4_derived.csv"

# Read one data file
data = pd.read_csv(raw_data_dir)
raw_data = data.values

for i in range(np.shape(raw_data)[0]):
    if abs(time0-1 - raw_data[i, 2:3]/1000) < 1:
        index_start = i
    elif abs(timeE - raw_data[i, 2:3]/1000) < 1:
        index_end = i
    else:
        continue

truncatedRawData_df = pd.DataFrame(raw_data[index_start+1:index_end+1,:])
truncatedRawData_df.to_csv("AllRoutesUG/"+file_name+"/Pixel4/Pixel4_derived.csv", header=data.columns, index=False)

# Read GT data
gt_data_dir = "RouteUS4O_G/"+file_name+"/Pixel4/ground_truth.csv"

# Read one data file
gt_data_file = pd.read_csv(gt_data_dir)
gt_data = gt_data_file.values

for i in range(np.shape(gt_data)[0]):
    if abs(time0-1 - gt_data[i, 2:3]/1000) < 1:
        index_start = i
    elif abs(timeE - gt_data[i, 2:3]/1000) < 1:
        index_end = i
    else:
        continue

truncatedRawData_df = pd.DataFrame(gt_data[index_start+1:index_end+1,:])
truncatedRawData_df.to_csv("AllRoutesUG/"+file_name+"/Pixel4/ground_truth.csv", header=gt_data_file.columns, index=False)
        
