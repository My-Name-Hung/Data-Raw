#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


import pandas as pd


# In[29]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


netflix_titles_df = pd.read_csv('netflix_titles.csv')
netflix_titles_df.head() # Import datadataset with type file csv and read dataset with all head have dataset


# In[31]:


netflix_titles_df.info()  #See infomation values


# In[32]:


netflix_titles_df.nunique() #See how much values DISTINCT


# In[33]:


netflix_titles_df.isnull().values.any() #See dataset contains values NULL?


# In[34]:


netflix_titles_df.isnull().sum().sum() #Caluculate sum all values NULL in dataset


# In[35]:


sns.heatmap(netflix_titles_df.isnull(), cbar = True)
plt.title('NULL Values Heatmap')
plt.show() # VISUALIZATION values NULL in dataset passed by heatmap and matplotlib


# In[36]:


netflix_titles_df.isnull().sum() #SUM values NULL COLUMN in dataset


# In[37]:


netflix_titles_df['director'].fillna('No Director', inplace = True)
netflix_titles_df['cast'].fillna('No cast', inplace = True)
netflix_titles_df['country'].fillna('Country Unavailable', inplace = True)
netflix_titles_df.dropna(subset = ['date_added','rating'], inplace = True)  # FIll NULL column in dataset replace new values and drop NULL with a column in dataset


# In[38]:


netflix_titles_df.isnull().any() # View Values NULL in dataset and we see no one column contains values NULL


# In[39]:


netflix_movie_df=netflix_titles_df[netflix_titles_df['type'] == 'Movie'].copy()
netflix_movie_df.head()


# In[40]:


# Rename type object in column duration and replace type object to string to rename time to seasons
# last replace type string to type integer for time one film unit minute 
netflix_movie_df.duration = netflix_movie_df.duration.astype(str).str.replace('min','').astype(int)
netflix_shows_df = netflix_movie_df
netflix_shows_df.rename(columns = {'duration':'seasons'}, inplace =True)
netflix_shows_df.replace({'seasons':{'1 Season': '1 Seasons'}},inplace = True)
netflix_shows_df.seasons = netflix_shows_df.seasons.astype(str).str.replace('Seasons','').astype(int) 


# In[41]:


netflix_titles_df.head()


# In[42]:


# Visualization count values for two types Movie/TV show in dataframe
# Figure raw chart and figsize have(width, height unit inch)
plt.figure(figsize=(7,5))
g = sns.countplot(netflix_titles_df.type, palette = 'pastel');
plt.title('Count of Movies and TV Shows')
plt.xlabel('Type (Movie/TV Show)')
plt.ylabel('Total Count')
plt.show()


# In[ ]:




