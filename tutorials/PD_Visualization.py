#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv(r"C:\Users\GWX-DATA\Downloads\ALEX THE ANALYST\Ice Cream Ratings.csv", index_col = 'Date')
df


# In[6]:


df.plot(kind = 'line')


# In[8]:


df.plot(kind = 'line', subplots = True)


# In[34]:


print(plt.style.available)
plt.style.use('dark_background')


# In[35]:


df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')


# In[12]:


df.plot(kind = 'bar')


# In[13]:


df.plot(kind = 'bar', stacked = True)


# In[17]:


df['Flavor Rating'].plot(kind = 'bar', stacked = True)


# In[15]:


df['Texture Rating'].plot(kind = 'bar', stacked = True)


# In[16]:


df['Overall Rating'].plot(kind = 'bar', stacked = True)


# In[18]:


df.plot.barh(stacked = True)


# In[21]:


df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 100, c = 'green' )


# In[23]:


df.plot.hist(bins = 10)


# In[26]:


df.boxplot()


# In[28]:


df.plot.area(figsize = (10,5))


# In[30]:


df.plot.pie(y = 'Overall Rating',figsize = (10,5))


# In[ ]:




