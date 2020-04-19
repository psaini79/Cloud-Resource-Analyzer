#!/usr/bin/env python

import pickle
import settings
from database import  getDatafromDb
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

def linearRegression(xtest):
    pickleModel = settings.ML_LR_MODEL
    pickle_in = open(pickleModel, "rb")
    loadData = pickle.load(pickle_in)
    dataset = loadData.predict(xtest)
    return dataset

def randomForest(xtest):
    pickleModel = settings.ML_RF_MODEL
    pickle_in = open(pickleModel, "rb")
    loadData = pickle.load(pickle_in)
    dataset = loadData.predict(xtest)
    return dataset

def arimaPrediction(ytest):
    pickleModel = settings.ML_ARIMA_MODEL
    pickle_in = open(pickleModel, "rb")
    loadData = pickle.load(pickle_in)
    print("test")
    print(ytest)
    print(loadData)
    #history = [x for x in loadData]
    predictions = list()
    for t in range(len(ytest)):
        # model = ARIMA(loadData, order=(5, 1, 0))
        model_fit = loadData.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat[0])
        obs = ytest[t]
       # history.append(obs)
    return predictions

if __name__ == "__main__":
    dataFrame = getDatafromDb()
    #predicted_data = linearRegression(xtest)
    print(dataFrame)
