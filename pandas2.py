#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv("universities.csv")
df


# # Conditional selection of the table values

# In[7]:


df[(df["GradRate"]>= 95) & (df["SFRatio"]<=12)]


# # Sort table by values

# In[9]:


df.sort_values(ascending=False,by="SFRatio")


# In[11]:


df.sort_values(by="SFRatio",ascending=False)


# # Use groupby() to find aggregated values

# In[13]:


sal = pd.read_csv("salaries.csv")
sal


# In[17]:


sal["salary"].groupby(sal["rank"]).mean()


# In[18]:


sal["salary"].groupby(sal["rank"]).sum()


# In[19]:


sal["salary"].groupby(sal["rank"]).median()


# In[20]:


sal[["salary","phd","service"]].groupby(sal["rank"]).mean()


# # Reshaping the dataframe with pivot()

# In[26]:


import pandas as pd
data = {
    'User ID' : [1,1,2,2,3,3,4,3,7],
    'Movie Name' : ['Inception', 'Titanic', 'Hi nanna', 'Avatar','Anand','Godavari','SVSC','YO','Murari'],
    'Rating' : [9,8,7,10,9,8,7,8,9]
}
df = pd.DataFrame(data)

pivot_table = df.pivot(index = 'User ID', columns = 'Movie Name', values = 'Rating')

print(pivot_table)


# In[ ]:




