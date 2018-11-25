# coding: utf-8

import pandas as pd
import numpy as np

df = pd.read_csv("/data/bikeshare/data/nyc/nyc.csv")
station_df = pd.read_json("/data/bikeshare/data/nyc/stations.json")

# birth year
birth_year = df['birth year']
df['birth year'] = df['birth year'].replace(r"\N", "NaN")
df['birth year']= df['birth year'].replace("NaN", np.nan)
df['birth year'] = pd.to_numeric(df['birth year'],  errors='coerce')

# trip duration
df['tripduration'] = df['tripduration']/60
df['gender'] = df['gender'].astype(str)
df['gender'] = df['gender'].replace(["0", "1", "2"], ["Unknown", "Male", "Female"])
df['usertype'] = df['usertype'].replace(["Subscriber", "Customer"], ["Member", "Non-member"])

# column rename
column_rename = {'tripduration': 'duration', 'starttime': 'start_time', 'stoptime': 'end_time', 'start station id': 'start_station_id', 'start station name': 'start_station', 'start station latitude': 'start_lat', 'start station longitude': 'start_lng', 'end station longitude': 'end_lng', 'end station latitude': 'end_lat', 'end station id': 'end_station_id', 'end station name': 'end_station', 'birth year': 'birth_year', 'usertype': 'user_type'}
df_renamed = df.rename(columns = column_rename)
df_renamed.head()
df_renamed = df_renamed[['duration','start_time','end_time', 'start_station', 'end_station', 'start_lng', 'end_lng', 'start_lat', 'end_lat', 'user_type', 'birth_year', 'gender']]

start_station = df_renamed['start_station']
end_station = df_renamed['end_station']

df = df_renamed

path = '/data/bikeshare/data/unified/'
df.to_csv(path+'nyc.csv', encoding='utf-8')