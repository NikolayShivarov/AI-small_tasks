# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 12:30:42 2023

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

df1_2018 = df1[(df1["Code"].notna()) & (df1["Year"] == 2018)]
countryLifeExp2018 = df1_2018[["Entity", "Life expectancy (period) at birth - Sex: all - Age: 0"]]

df2_2018 = df2[(df2["Code"].notna()) & (df2["Year"] == 2018)]
countryGdp2018 = df2_2018 [["Entity", "GDP per capita"]]

df3_2018 = df3[(df3["Code"].notna()) & (df3["Year"] == 2018)]
Gdp2018 = df3_2018 [["Entity", "GDP, PPP (constant 2017 international $)"]]

gdpLe2018 = pd.merge(countryLifeExp2018, countryGdp2018, on="Entity")
gdpLe2018overall = pd.merge(countryLifeExp2018, Gdp2018, on="Entity")

##A
plt.scatter(gdpLe2018["Life expectancy (period) at birth - Sex: all - Age: 0"], gdpLe2018["GDP per capita"])
plt.title("GDP and Life expectancy in 2018")
plt.xlabel("Life expectancy")
plt.ylabel("GDP per capita in US dollars")
##B
averageAge = countryLifeExp2018["Life expectancy (period) at birth - Sex: all - Age: 0"].mean()
standardDeviationAge = countryLifeExp2018["Life expectancy (period) at birth - Sex: all - Age: 0"].std()
highAge = averageAge + standardDeviationAge
countriesHigherLifeExpectancy = countryLifeExp2018[countryLifeExp2018["Life expectancy (period) at birth - Sex: all - Age: 0"] > highAge ]
print(countriesHigherLifeExpectancy[["Entity","Life expectancy (period) at birth - Sex: all - Age: 0"]])
##C
poorCountriesGdp = countryGdp2018["GDP per capita"].quantile(0.45)
highLifeExpectancy = countryLifeExp2018["Life expectancy (period) at birth - Sex: all - Age: 0"].quantile(0.6)
highLifePoor = gdpLe2018[(gdpLe2018["GDP per capita"] <= poorCountriesGdp) & (gdpLe2018["Life expectancy (period) at birth - Sex: all - Age: 0"] >= highLifeExpectancy)]
print(highLifePoor[["Entity","Life expectancy (period) at birth - Sex: all - Age: 0","GDP per capita"]])
##D
richCountriesOverallGdp = Gdp2018["GDP, PPP (constant 2017 international $)"].quantile(0.8)
richCountriesOverall = gdpLe2018overall[gdpLe2018overall["GDP, PPP (constant 2017 international $)"] > richCountriesOverallGdp]
richCountriesOverallHighLife = richCountriesOverall[richCountriesOverall["Life expectancy (period) at birth - Sex: all - Age: 0"] > highLifeExpectancy]
##E
richCountriesGdp = countryGdp2018["GDP per capita"].quantile(0.8)
richCountries = gdpLe2018[gdpLe2018["GDP per capita"] > richCountriesGdp]
richCountriesHighLife = richCountries[richCountries["Life expectancy (period) at birth - Sex: all - Age: 0"] > highLifeExpectancy]

print(gdpLe2018[gdpLe2018["Entity"] == "Bulgaria"])





