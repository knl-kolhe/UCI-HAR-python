# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 00:53:24 2018

@author: Kunal
"""

#import training dataset
X = open('UCI HAR Dataset\\train\\X_train.txt')
y = open('UCI HAR Dataset\\train\\y_train.txt')

#X_train contains training values
X_temp = X.read()
X_t1=X_temp.split('\n')
del X_temp
r=len(X_t1)-1
c=X_t1[0].count(' ')+1

import numpy
X_train = numpy.zeros((7352, 562))

for i in range(0,r):
    X_temp = X_t1[i].split(' ')
    X_temp[0]=1
    for j in range(0,c):
        X_train[i,j]=float(X_temp[j])
    del X_temp
del X_t1,r,c,i,j

#y_train contains training labels
y_temp = y.read()
y_train = (y_temp.split('\n'))

for item in y_train:
    float(item)
del item,y_temp

#importing test dataset
Xtest = open('UCI HAR Dataset\\test\\X_test.txt')
ytest = open('UCI HAR Dataset\\test\\y_test.txt')

#X_test contains test values
X_temp = Xtest.read()
X_t1 = X_temp.split('\n')
r = len(X_t1) - 1
c = X_t1[0].count(' ') + 1

X_test = numpy.zeros((r,c))

for i in range(0,r-1):
    X_temp = X_t1[i].split(' ')
    X_temp[0]=1
    for j in range(0,len(X_temp)):
        X_test[i,j]=float(X_temp[j])
    del X_temp
del X_t1,c,i,j,r

y_temp = ytest.read()
y_test = (y_temp.split('\n'))

for item in y_test:
    float(item)
del item,y_temp

#run the logistic regression
from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression(C=2.0)

import time
start = time.time()

logistic.fit(X_train,y_train)

end = time.time()

print("Time Required to train: {}".format(end-start))

start = time.time()

y_pred = logistic.predict(X_test)

end = time.time()

print("Time Required to test: {}".format(end-start))

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
#confusion_matrix  #to print confusion matrix

sum=0;
for i in range(0,6):
    sum += confusion_matrix[i,i]
del i

print("Exact number of accurate predictions in test set: {}/{}".format(sum,len(X_test)))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))