#!/usr/bin/env python
# coding: utf-8

# In[428]:


import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as sts 
print("All set!")


# In[430]:


# data = pd.read_csv(r"/Users/bijayamanandhar/Desktop/us_covid_analysis/us_counties_covid19_daily.csv")

with open('us_counties_covid19_daily.csv', 'r') as csv_file:
    n = 15000
    data = pd.read_csv(csv_file, skiprows = lambda i: i % n != 0)


# In[431]:


df = pd.DataFrame(data)


# In[432]:


n = data.to_numpy()
nd = n.tolist()


# In[434]:


state_cases = dict()
state_deaths = dict()
country_cases = 0
country_deaths = 0
for row in nd:
    country_cases += row[4]
    if row[2] not in state_cases:
        state_cases[row[2]] = row[4]       
    else:
        state_cases[row[2]] += row[4]  
        
for row in nd:
    country_deaths += row[5]
    if row[2] not in state_deaths:
        state_deaths[row[2]] = row[5]
    else:
        state_deaths[row[2]] += row[5]
print('Country Cases: {}\nCountry Deaths: {}'.format(country_cases, country_deaths))


# In[437]:


# sd = pd.Series(d)


# In[438]:


x = input('State: ')
print('Total Cases: {}\nTotal Deaths: {}'.format(state_cases[x], state_deaths[x]))


# In[439]:


x, y = [], []
for k in state_cases:
    x.append(k)
    y.append(state_cases[k])
    


# In[440]:


plt.figure(figsize=(20,10))
plt.bar(x, y)
plt.xticks(x, x, rotation=65)
plt.show()


# In[397]:


with open('us_covid19_daily.csv', 'r') as csv_file1:
    data1 = pd.read_csv(csv_file1)
    


# In[399]:


with open('us_states_covid19_daily.csv', 'r') as csv_file1:
    data2 = pd.read_csv(csv_file1)


# In[421]:


from dataclasses import make_dataclass
Point = make_dataclass("Point", [("x", int), ("y", int)])
d = pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
d


# In[422]:


type(d)


# In[426]:


d.to_numpy().tolist()


# In[ ]:




