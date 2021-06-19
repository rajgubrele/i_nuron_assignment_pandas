#!/usr/bin/env python
# coding: utf-8

# ##
# ***Assignment Pandas inuron***
# ##

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
df


# 1. Some values in the the FlightNumber column are missing. These numbers are 
# meant to increase by 10 with each row so 10055 and 10075 need to be put in 
# place. Fill in these missing numbers and make the column an integer column 
# (instead of a float column).

# In[5]:


df.iloc[1,1] =10055 
df.iloc[3,1] = 10075
df['FlightNumber'] =df['FlightNumber'].astype(int) 
df


# 2. The From_To column would be better as two separate columns! Split each 
# string on the underscore delimiter _ to give a new temporary DataFrame with 
# the correct values. Assign the correct column names to this temporary 
# DataFrame.

# In[6]:


df[['From', 'To']]= df.From_To.str.split("_",expand=True)

df


# In[7]:


df1 = df[['From','To','FlightNumber','Airline','RecentDelays']]
df1


# 3. Notice how the capitalisation of the city names is all mixed up in this 
# temporary DataFrame. Standardise the strings so that only the first letter is 
# uppercase (e.g. "londON" should become "London".)

# In[8]:


df1['From'] = df1['From'].str.capitalize()
df1['To'] = df1['To'].str.capitalize()

df1


# 4. Delete the From_To column from df and attach the temporary DataFrame 
# from the previous questions.

# In[9]:


df1

