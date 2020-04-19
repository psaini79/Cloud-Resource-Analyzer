#!/usr/bin/env python
from sklearn.linear_model import LinearRegression
import pickle
from database import getDatafromDb
from dataprocessor import processDbDataForLrTestInput
from dataprocessor import prepareData
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.arima_model import ARIMA

def buildLinearRegressionModel():
    dataFrame = getDatafromDb(-1)
    dataFrame = processDbDataForLrTestInput(dataFrame)
    X_train, y_train = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def buildRandomForestMNodel():
    dataFrame = getDatafromDb(-1)
    dataFrame = processDbDataForLrTestInput(dataFrame)
    X_train, y_train = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model


def buildArimaModel():
    dataFrame = getDatafromDb(-1)
    dataFrame = processDbDataForLrTestInput(dataFrame)
    X_train, y_train = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
    history = [x for x in y_train]
    predictions = list()
    for t in range(len(y_train)):
        model = ARIMA(history, order=(5, 1, 0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat[0])
        obs = y_train[t]
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
    return model

def saveModel(model, name):
    pickle.dump(model, open(name, 'wb'))

