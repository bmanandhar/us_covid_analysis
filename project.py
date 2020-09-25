import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# data = pd.read_csv(r"us_counties_covid19_daily.csv")
#date     county       state     fips  cases  deaths
# print(data.tail())
# print(data.describe())

#date,county,state,fips,cases,deaths
sum = 0
x = input("Enter county name: ")
with open("/Users/bijayamanandhar/Desktop/us_covid_analysis/us_counties_covid19_daily.csv","r") as data:
    csv_reader = csv.reader(data)
    next(csv_reader)
    for line in csv_reader:
        if x == line[1]:
            sum += int(line[4])
    print(x,"Cases: ", sum)

