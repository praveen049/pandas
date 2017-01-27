#! /usr/bin/python

import pandas as pd 

ufo = pd.read_csv("http://bit.ly/uforeports")

print ufo.tail()

print ufo.isnull().tail()

print ufo.isnull().sum()

# if any column is empty
print ufo.dropna(how='any').shape
# if all columns is empty
print ufo.dropna(how='all').shape