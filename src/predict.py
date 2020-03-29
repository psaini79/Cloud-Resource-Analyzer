#!/usr/bin/env python

import pickle
from settings import ML_LR_MODEL

def linearRegression(xtest):
    pickleModel = ML_LR_MODEL
    pickle_in = open(pickleModel, "rb")
    loadData = pickle.load(pickle_in)
    dataset = loadData.predict(xtest)
    return dataset

