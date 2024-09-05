# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:37:32 2023

@author: Nikolay Shivarov
"""

import pandas as pd
import numpy 
import matplotlib.pyplot as plt
from pandas.plotting import table

df1 = pd.read_csv("life-expectancy.csv")
df2 = pd.read_csv("gdp-per-capita-maddison.csv")
df3 = pd.read_csv("national-gdp-wb.csv")

pd.set_option("display.max_rows", None, "display.max_columns", None)

df1_1998 = df1[(df1["Code"].notna()) & (df1["Year"] == 1998)]
countryLifeExp1998 = df1_1998[["Entity", "Life expectancy (period) at birth - Sex: all - Age: 0"]]

df2_1998 = df2[(df2["Code"].notna()) & (df2["Year"] == 1998)]
countryGdp1998 = df2_1998 [["Entity", "GDP per capita"]]

df3_1998 = df3[(df3["Code"].notna()) & (df3["Year"] == 1998)]
Gdp1998 = df3_1998 [["Entity", "GDP, PPP (constant 2017 international $)"]]

gdpLe1998 = pd.merge(countryLifeExp1998, countryGdp1998, on="Entity")
gdpLe1998overall = pd.merge(countryLifeExp1998, Gdp1998, on="Entity")

##A
plt.scatter(gdpLe1998["Life expectancy (period) at birth - Sex: all - Age: 0"], gdpLe1998["GDP per capita"])
plt.title("GDP and Life expectancy in 1998")
plt.xlabel("Life expectancy")
plt.ylabel("GDP per capita in US dollars")
##B
averageAge = countryLifeExp1998["Life expectancy (period) at birth - Sex: all - Age: 0"].mean()
standardDeviationAge = countryLifeExp1998["Life expectancy (period) at birth - Sex: all - Age: 0"].std()
highAge = averageAge + standardDeviationAge
countriesHigherLifeExpectancy = countryLifeExp1998[countryLifeExp1998["Life expectancy (period) at birth - Sex: all - Age: 0"] > highAge ]
print(countriesHigherLifeExpectancy[["Entity","Life expectancy (period) at birth - Sex: all - Age: 0"]])
##C
poorCountriesGdp = countryGdp1998["GDP per capita"].quantile(0.45)
highLifeExpectancy = countryLifeExp1998["Life expectancy (period) at birth - Sex: all - Age: 0"].quantile(0.6)
highLifePoor = gdpLe1998[(gdpLe1998["GDP per capita"] <= poorCountriesGdp) & (gdpLe1998["Life expectancy (period) at birth - Sex: all - Age: 0"] >= highLifeExpectancy)]
print(highLifePoor[["Entity","Life expectancy (period) at birth - Sex: all - Age: 0","GDP per capita"]])
##D
richCountriesOverallGdp = Gdp1998["GDP, PPP (constant 2017 international $)"].quantile(0.8)
richCountriesOverall = gdpLe1998overall[gdpLe1998overall["GDP, PPP (constant 2017 international $)"] > richCountriesOverallGdp]
richCountriesOverallHighLife = richCountriesOverall[richCountriesOverall["Life expectancy (period) at birth - Sex: all - Age: 0"] > highLifeExpectancy]
##E
richCountriesGdp = countryGdp1998["GDP per capita"].quantile(0.8)
richCountries = gdpLe1998[gdpLe1998["GDP per capita"] > richCountriesGdp]
richCountriesHighLife = richCountries[richCountries["Life expectancy (period) at birth - Sex: all - Age: 0"] > highLifeExpectancy]


