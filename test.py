import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as sts 
print("All set!")


with open('us_counties_covid19_daily.csv', 'r') as csv_file:
    n = 15000
    data = pd.read_csv(csv_file, skiprows = lambda i: i % n != 0)
print(data)