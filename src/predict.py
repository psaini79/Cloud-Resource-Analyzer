#!/usr/bin/env python

import pickle
from sklearn.preprocessing import StandardScaler
from settings import ML_LR_MODEL
from database import  getDatafromDb

def linearRegression(xtest):
    pickleModel = ML_LR_MODEL
    pickle_in = open(pickleModel, "rb")
    loadData = pickle.load(pickle_in)
    dataset = loadData.predict(xtest)
    return dataset

if __name__ == "__main__":
    dataFrame = getDatafromDb()
    #predicted_data = linearRegression(xtest)
    print(dataFrame)
