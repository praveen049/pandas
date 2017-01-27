#! /usr/bin/python

import pandas as pd 

orders = pd.read_table('http://bit.ly/chiporders')
print orders.item_name.str.upper().head()

print orders.columns

print orders.choice_description.str.upper().head()

print orders.choice_description.str.replace('[\[\]]','').head()

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print drinks.dtypes

drinks = pd.read_csv('http://bit.ly/drinksbycountry',dtype={'beer_servings':float})
print drinks.dtypes
print drinks.groupby('continent').beer_servings.mean()

print drinks.groupby('continent').beer_servings.agg(['count','mean','max','min'])