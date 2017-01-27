#! /usr/bin/python

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
print movies.head()

print movies.describe()

print movies[20:25]

print movies.iloc[20]