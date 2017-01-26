#!/usr/bin/python

import pandas as pd

s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'], index = ['A','C','F','G','Z'])
print s
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print cities[2]
print cities.index.values