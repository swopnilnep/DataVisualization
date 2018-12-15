
# coding: utf-8

import pandas as pd

print("Importing the datasets...")

print("Importing Boston...")

boston = pd.read_csv("/data/bikeshare/data/unified/boston.csv")

print("Complete!")
print("Importing NYC...")

nyc = pd.read_csv("/data/bikeshare/data/unified/nyc.csv")

print("Complete!")

print("Processing...")

df = boston

print('Adding the two datasets..')

df = df.append(nyc, ignore_index=True, sort=True)

print("Complete!")

path = '/data/bikeshare/data/unified/'

print('Exporting to .. ' + path)

path = '/data/bikeshare/data/unified/'
df.to_csv(path+'merged.csv', encoding='utf-8')

print('Rows: {} Columns: {} Size: {}'.format(df.shape[0], df.shape[1], df.size))