
# coding: utf-8

# Author: Giang Nguyen <br>
# Organization: Luther College

# In[73]:


import pandas as pd
import numpy as np
import seaborn as sns
import folium
from folium import plugins
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap


# In[2]:


df = pd.read_csv("/data/bikeshare/data/nyc/nyc.csv")
station_df = pd.read_json("/data/bikeshare/data/nyc/stations.json")


# In[3]:


df


# * 10 most popular station
# * distribution of tripduration (plot)
# * geopandas (location map)

# In[4]:


station_df.head()


# In[5]:


df.describe()


# ## Transcription and Unification of Dataset

# In[53]:


df.dtypes


# ### Birth year column

# In[7]:


birth_year = df['birth year']


# In[8]:


df['birth year'] = df['birth year'].replace(r"\N", "NaN")


# In[9]:


df['birth year']


# In[10]:


df['birth year']= df['birth year'].replace("NaN", np.nan)


# In[11]:


df['birth year'] = pd.to_numeric(df['birth year'],  errors='coerce')


# ### Tripduration column

# In[12]:


df['tripduration'] = df['tripduration']/60


# In[13]:


df['tripduration']


# In[14]:


df.head()


# In[15]:


df['gender'] = df['gender'].astype(str)


# In[16]:


df['gender'] = df['gender'].replace(["0", "1", "2"], ["Unknown", "Male", "Female"])


# In[17]:


df.head()


# ### Usertype column

# In[18]:


df['usertype'] = df['usertype'].replace(["Subscriber", "Customer"], ["Member", "Non-member"])


# In[19]:


df['usertype']


# In[94]:


column_rename = {'tripduration': 'duration', 'starttime': 'start_time', 'stoptime': 'end_time', 'start station id': 'start_station_id', 'start station name': 'start_station', 'start station latitude': 'start_lat', 'start station longitude': 'start_lng', 'end station longitude': 'end_lng', 'end station latitude': 'end_lat', 'end station id': 'end_station_id', 'end station name': 'end_station', 'birth year': 'birth_year', 'usertype': 'user_type'}
df_renamed = df.rename(columns = column_rename)
df_renamed.head()


# In[102]:


df_renamed = df_renamed[['duration','start_time','end_time', 'start_station', 'end_station', 'start_lng', 'end_lng', 'start_lat', 'end_lat', 'user_type', 'birth_year', 'gender']]
df_renamed.head()


# ## 10 most popular station

# In[79]:


start_station = df_renamed['start_station']
start_station.value_counts()


# In[22]:


start_station.value_counts().head(10)


# In[80]:


end_station = df_renamed['end_station']
end_station.value_counts().head(10)


# ## Distribution of trip duration

# In[81]:


duration = df_renamed['duration']


# In[82]:


duration.describe()


# In[83]:


duration.hasnans


# In[84]:


duration_by_gender = df_renamed.groupby('gender')['duration'].sum()


# In[85]:


duration_by_gender


# In[86]:


#duration_by_gender_plot = sns.barplot(x = 'gender', y = 'tripduration', data = df)


# ### Gender and gender by usertype distribution

# In[87]:


gender = df_renamed['gender']


# In[88]:


gender.value_counts()


# In[98]:


gender_plot = sns.countplot(x = 'gender', data = df_renamed)


# In[99]:


gender_by_usertype = sns.countplot(x = 'user_type', hue = 'gender', data = df_renamed)


# Throughout the bar plot, we can easily observe that the number of the make bikeshare is higher third times as that of the female bikeshare. Moreover, all female and male are subscriber (annual member) and all unknown people are customer (24-hour pass or 3-day pass user - non-member).

# ## Map of start station and end station

# In[91]:


start_station_name = df_renamed['start_station'].values
start_station_name


# In[67]:


stop_map = folium.Map(location = [40.735324, -73.998004], zoom_start = 11)
stop_map


# In[100]:


for index, row in df_renamed.iterrows():
    folium.CircleMaker([row['start_lat'], row['start_lng']], radius = 15, popup = row['start_station'], fill_color = "#3db7e4").add_to(stop_map)


# In[66]:


stops_heatmap = folium.Map(location=[40.735324, -73.998004], zoom_start=11)
stops_heatmap.add_child(plugins.HeatMap([[row["start station longitude"], row["start station latitude"]] for name, row in df.iloc[:50000].iterrows()]))
stops_heatmap.save("heatmap.html")
stops_heatmap

