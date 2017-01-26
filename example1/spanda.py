#! /usr/bin/python

import pandas as pd

data = {'year': [2010,2011,2012,2013,2014,2015,2016,2017],
        'team': ['nwg','nbg','nbg','fco','fco','fng','fng','net']}
        
#columns job is not listed to it will be NaN
mine = pd.DataFrame(data,columns=['year','job'])
print mine
mine = pd.DataFrame(data,columns=['year','team'])
print mine
imdb = pd.read_csv('http://bit.ly/imdbratings')
print imdb.head()
print imdb[imdb.duration > 200]
print imdb.index
print pd.read_table('http://bit.ly/chiporders').head()
user_cols = ['user_id','Age','Gender','Job','Zip']
print pd.read_table('http://bit.ly/movieusers',sep='|', header=None,names=user_cols).head()