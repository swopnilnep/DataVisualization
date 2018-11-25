# Swopnil N. Shrestha @swopnilnep
# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv("/data/bikeshare/data/boston/boston.csv")
stations = pd.read_csv("/data/bikeshare/data/boston/stations.csv")

df = df[['duration','start_date','end_date','strt_statn','end_statn','subsc_type','birth_date','gender']]

stations = stations.set_index('id')

# Merge start station data
df_start = df.merge(stations, left_on="strt_statn", right_index=True, how="left")

# Select end data
df_start = df_start[['duration','start_date','station','lat','lng','subsc_type','birth_date','gender']]

# Rename start columns
df_start = df_start.rename(columns={'start_date':'start_time','station':'start_station','lat':'start_lat','lng':'start_lng','subsc_type':'user_type','birth_date':'birth_year'})

# Merge end station data
df_end = df.merge(stations, left_on="end_statn", right_index=True, how="left")

# Select end data
df_end = df_end[['end_date','station','lat','lng']]

# Rename end columns 
df_end = df_end.rename(columns={'end_date':'end_time','station':'end_station', 'lat':'end_lat','lng':'end_lng'})
df_start[['end_time','end_station','end_lat','end_lng']] = df_end
df = df_start[['duration','start_time','end_time','start_station','end_station','start_lat','end_lat','start_lng','end_lng','user_type','birth_year','gender']]

# Change usertype to `member` and `non-member`

df.user_type.value_counts()

df['user_type'] = df.user_type.replace(['Registered', 'Casual'],['Member','Non-member'])

path = '/data/bikeshare/data/unified/'
df.to_csv(path+'boston.csv', encoding='utf-8')