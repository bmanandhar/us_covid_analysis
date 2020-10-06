import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = input("County: ")
county_sum = 0
with open("us_counties_covid19_daily.csv","r") as data:    
    csv_reader = csv.reader(data)
    next(csv_reader)
    for line in csv_reader:
        if x == line[1]:
            county_sum += int(line[4])            
    print(x,"Cases: ", county_sum)
if county_sum == 0:
        print("Either {} county doesn't have any case or you entered wrong spelling.".format(x))
