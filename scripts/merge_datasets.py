
# coding: utf-8

import pandas as pd

boston = pd.read_csv("/data/bikeshare/data/unified/boston.csv")
nyc = pd.read_csv("/data/bikeshare/data/unified/nyc.csv")
print("Processing...")

df = boston

df = df.append(nyc, ignore_index=True, sort=True)

print('Added the two datasets..')
print('Rows: {} Columns: {} Size: {}'.format(df.shape[0], df.shape[1], df.size))
path = '/data/bikeshare/data/unified/'

df.to_csv(path+'merged.csv', encoding='utf-8')

