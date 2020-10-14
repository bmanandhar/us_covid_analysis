#!/usr/bin/env python
# coding: utf-8

# In[1]:


#covid_analysis

import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as sts 
from statistics import stdev
print("All set!")


# In[55]:


#data for test
#Index(['date', 'county', 'state', 'fips', 'cases', 'deaths'], dtype='object')
with open('/Users/bijayamanandhar/Desktop/data/us_counties_covid19_daily.csv', 'r') as csv_file:
    n = 15000
    data = pd.read_csv(csv_file, skiprows = lambda i: i % n != 0)
data.describe()


# In[3]:


#convert data to numpy array, then to python list
n = data.to_numpy()
nd = n.tolist()


# In[4]:


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


# In[53]:


x = input('Enetr state name: ')
data.loc[data['state'] == x, ['cases', 'deaths']].sum()


# In[6]:


#bar graph

plt.figure(figsize=(20, 10))
x = list(state_cases.keys())
y = list(state_cases.values())
plt.bar(x, y)
plt.xticks(x, x, rotation=65)
plt.show()


# In[7]:


pd.DataFrame(list(country_data.items())).info()


# In[8]:


pd.DataFrame(list(country_data.items())).dtypes


# In[9]:


type(pd.DataFrame(list(country_data.items())))


# In[12]:


data.dtypes


# In[13]:


data['date'].shape


# In[15]:


data['state'].shape


# In[16]:


data.shape


# In[18]:


data["date"] = pd.to_datetime(data["date"])


# In[28]:


data.mean(axis=0)


# In[21]:


data.columns


# In[27]:


get_ipython().run_cell_magic('HTML', '', '<style type="text/css">\ntable.dataframe td, table.dataframe th {\n    border: 1px  black solid !important;\n  color: black !important;\n}\n</style>')


# In[30]:


data.state.describe()


# In[31]:


data.cases.mean()


# In[32]:


data.deaths.mean()


# In[33]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


data.groupby('state').mean().plot(kind='bar')
#<matplotlib.axes._subplots.AxesSubplot at 0x7fd200da02b0>


# In[38]:


pd.crosstab(data.state, data.date)


# In[39]:


data.drop(3, axis=0).head() 
#drops the data row at index 3, axis-0 means across rows (top-down)


# In[43]:


data.isnull().sum() 
#shows total number of missing data, True=1, False=0 


# In[45]:


data.drop('fips', axis=1).head(5)
#drops column 'fips', axis=1, means across column (left-right)


# In[51]:


#Standard Deviatiion
standard_deviation = stdev(list(data.cases))
standard_deviation


# In[54]:


max(data.cases) #max number in cases clomun


# In[55]:


min(data.cases)#min number in cases column


# In[56]:


max(data.deaths)


# In[57]:


min(data.deaths)


# In[58]:


np.std(data.cases)


# In[61]:


data[data.state == 'California'].mean() 
#gives totals of numerical columns for a specified state


# In[63]:


data.cases.sum() #total for a specified column


# In[4]:


data.head()


# In[ ]:




