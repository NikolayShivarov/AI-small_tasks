# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:35:08 2023

@author: Nikolay Shivarov
"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix

## Loading the data from Iris
iris = load_iris()
data = iris.data
target = iris.target

## spliting the data into a training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(data, target)

## Creating a logistic regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train, Y_train)

## Making a prediction on the test data
Y_predict = logistic_model.predict(X_test)

## Creating the confusion matrix
confusionMatrix = confusion_matrix(Y_test, Y_predict)
print(confusionMatrix)

