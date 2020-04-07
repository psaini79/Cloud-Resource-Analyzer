#!/usr/bin/env python
from sklearn.linear_model import LinearRegression
import pickle
from settings import ML_LR_MODEL
from database import getDatafromDb
from dataprocessor import processDbDataForLrTestInput
from dataprocessor import prepareData

def buildLinearRegressionModel():
    dataFrame = getDatafromDb(-1)
    dataFrame = processDbDataForLrTestInput(dataFrame)
    X_train, y_train = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def saveModel(model):
    pickle.dump(model, open(ML_LR_MODEL, 'wb'))

