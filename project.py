import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"us_counties_covid19_daily.csv")
print(data.head())
#date     county       state     fips  cases  deaths
print(data.columns)
print(data.tail())