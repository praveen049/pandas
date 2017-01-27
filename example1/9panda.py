#! /usr/bin/python

import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('http://bit.ly/kaggletrain')

print train.head()
print train.columns

feature_cols = ['Pclass','Parch']
X = train.loc[:,feature_cols]
print X.head()
y= train.Survived

logreg = LogisticRegression()
logreg.fit(X,y)

test = pd.read_csv('http://bit.ly/kaggletest')

X_new = test.loc[:,feature_cols]
print X_new.shape

new_pred_class = logreg.predict(X_new)

print new_pred_class

print  pd.DataFrame({'PassenderId':test.PassengerId,'Survived':new_pred_class})