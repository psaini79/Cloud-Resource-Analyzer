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

def arimaPrediction(ytest, history):
    pickleModel = settings.ML_ARIMA_MODEL
    pickle_in = open(pickleModel, "rb")
    loadData = pickle.load(pickle_in)
    print(loadData)
    predictions = list()
    print(len(history))
    for t in range(len(ytest)): 
        model = ARIMA(history, order=(5,1,0)) 
        model_fit = model.fit(disp=0)
        output = model_fit.forecast() 
        yhat = output[0] 
        predictions.append(yhat[0]) 
        obs = ytest[t] 
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
    return predictions 

if __name__ == "__main__":
    dataFrame = getDatafromDb()
    #predicted_data = linearRegression(xtest)
    print(dataFrame)
