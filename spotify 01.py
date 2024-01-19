#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df1 = pd.read_csv(r'C:\Users\arinc\OneDrive\Desktop\final_tracks.csv')
df2 = pd.read_csv(r"C:\Users\arinc\OneDrive\Desktop\main_dataset.csv")


# In[3]:


df1.head().T


# In[4]:


df1.drop(columns = ['playlist_uris', 'playlist_uris', 'track_uri', 'Unnamed: 0'], inplace = True)


# In[5]:


df1.info()


# In[ ]:





# In[7]:


df1.head()


# In[8]:


df1.dropna


# In[10]:


df1 = pd.DataFrame(df1)


# In[14]:


df1.isnull().sum()


# In[19]:


df1 = df1.dropna()


# In[20]:


df1.shape


# In[22]:


df2.isnull().sum()


# In[23]:


df2.dropna()


# In[ ]:


df2.

