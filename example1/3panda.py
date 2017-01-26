#! /usr/bin/python

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
print ufo.head()
print ufo.columns

ufo.rename(columns={'Colors Reported':'Colors_reported','Shape Reported':'Shape_reported'},inplace='True')
print ufo.columns
ufo_cols=['city','colors','shape','state','time']
ufo.columns = ufo_cols
print ufo.columns
#header=0 means the 0th in the list is the header
ufo = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols,header=0)
print ufo.head()
ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.columns = ufo.columns.str.replace(' ','_')
print ufo.head()
