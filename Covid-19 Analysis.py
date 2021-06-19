#!/usr/bin/env python
# coding: utf-8

# # Covid-19 India Analysis

# 

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


data = pd.read_csv(r"E:\Covid-19\covid_19_india.csv")


# In[5]:


data


# In[6]:


data.head()


# In[7]:


data.tail()


# In[9]:


data.isnull().sum()


# In[10]:


data.describe()


# In[11]:


data.columns


# # Relating the Variables with Scatterplot
# 

# In[12]:


sns.replot(x="State/UnionTerritory",y="ConfirmedIndianNational")


# In[13]:


sns.relplot(x="State/UnionTerritory",y="ConfirmedIndianNational",data=data)


# In[14]:


sns.relplot(x="Confirmed",y="Cured",data=data)


# In[15]:


sns.pairplot(data)


# In[16]:


sns.relplot(x="Confirmed",y="Cured",hue="Deaths",data=data)


# In[17]:


sns.relplot(x="Deaths",y="Cured",hue="Confirmed",data=data)


# In[18]:


sns.relplot(x="Deaths",y="Cured",kind = "Line",data=data)


# In[19]:


sns.relplot(x="Deaths",y="Cured",kind = Line,data=data)


# In[20]:


sns.relplot(x="Deaths",y="Cured",kind = "line",data=data)


# In[ ]:





# In[ ]:




