# -*- coding: utf-8 -*-
"""
Author: Nikolay Shivarov
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns


## reading the csv
df = pd.read_csv("data_assignment2.csv")
## removing the unnecesary columns
areaPrice = df[["Living_area","Selling_price"]]

## creating a linear regression
LR = LinearRegression()
LR.fit(areaPrice["Living_area"].values.reshape(-1,1),areaPrice["Selling_price"].values.reshape(-1,1))

## calculating the intercept and the slope
print("The intercept is: ", LR.intercept_[0])
print("The slope is: ", LR.coef_[0][0])

## calculating the estimated price for 100, 150, 200 sq m
print("Estimated price for 100m^2: " , LR.predict(np.array([[100]]))[0][0])
print("Estimated price for 150m^2: " , LR.predict(np.array([[150]]))[0][0])
print("Estimated price for 200m^2: " , LR.predict(np.array([[200]]))[0][0])

## creating a residual plot
sns.residplot(x='Living_area', y='Selling_price', data=areaPrice)
