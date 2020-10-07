#!/usr/bin/env python
# coding: utf-8

# In[91]:


import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as sts 
print("All set!")


# In[300]:


# data = pd.read_csv(r"/Users/bijayamanandhar/Desktop/us_covid_analysis/us_counties_covid19_daily.csv")

#data for test
with open('us_counties_covid19_daily.csv', 'r') as csv_file:
    n = 1500
    data = pd.read_csv(csv_file, skiprows = lambda i: i % n != 0)
print(type(data))
print(data.info())


# In[93]:


df = pd.DataFrame(data)


# In[44]:


n = df.to_numpy()
nd = n.tolist()


# In[205]:


state_cases = dict()
state_deaths = dict()
country_data = dict()
country_cases = 0
country_deaths = 0

for row in nd:
    
    if row[2] not in state_cases:
        state_cases[row[2]] = row[4]
    else:
        state_cases[row[2]] += row[4]

    if row[2] not in state_deaths:
        state_deaths[row[2]] = row[5]
    else:
        state_deaths[row[2]] += row[5]
   
cases = sum(state_cases.values())
deaths = sum(state_deaths.values())
case_list = list(state_cases.values())
country_data['cases'] = sum(state_cases.values())
country_data['death'] = sum(state_deaths.values())
country_data['mean'] = round(np.mean(case_list))
country_data['median'] = np.median(case_list)

pd.DataFrame(list(country_data.items()))




# In[95]:


state_data = dict()
x = input('State: ')
if x in state_cases:
    state_data['Cases'] = int(state_cases[x])
    state_data['Deaths'] = int(state_deaths[x])
    state_data['Percent'] = round((state_cases[x]/cases)*100, 2)
    state_data['Case to Death Percent'] = round((state_deaths[x]/state_cases[x])/100, 4)

else:
    print('Either state name is wrong or it has no cases yet!')
pd.DataFrame(list(state_data.items()))


# In[220]:


#bar graph
# fig, axs = plt.subplots(figsize=(12, 4))

plt.figure(figsize=(20, 10))
x = list(state_cases.keys())
y = list(state_cases.values())
plt.bar(x, y)
plt.xticks(x, x, rotation=65)
plt.show()


# In[161]:


pd.DataFrame(list(country_data.items())).info()


# In[164]:


pd.DataFrame(list(country_data.items())).dtypes


# In[165]:


type(pd.DataFrame(list(country_data.items())))


# In[166]:


df.dtypes


# In[167]:


df['date'].shape


# In[168]:


df['state'].shape


# In[169]:


df.shape


# In[221]:


df["date"] = pd.to_datetime(df["date"])


# In[237]:


# fig, axs = plt.subplots(figsize=(12, 4))


# In[ ]:




