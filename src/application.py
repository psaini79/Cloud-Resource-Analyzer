#!flask/bin/python
import os
import json

from flask import Flask
from flask import request
from settings import SECRET_KEY
from predict import linearRegression
from database import getDatafromDb, writeDataToDb
from models import buildLinearRegressionModel
from models import saveModel
from dataprocessor import processDbDataForLrTestInput
from dataprocessor import prepareData

application = Flask(__name__)
application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 
application.config['SESSION_TYPE'] = SECRET_KEY

@application.route('/')
def home():
   print("This is CRA ML Analyser")
   return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


@application.route('/trigger_ml', methods=['POST'])
def triggerML():
    error = None
    if request.method == 'POST':
        #tenantname = request.form['tenant_name']
        period = request.form['period']
        #interval = request.form['interval']
        dataFrame = getDatafromDb()
        dataFrame = processDbDataForLrTestInput(dataFrame)
        X_test, y_test = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
        predictedData = linearRegression(X_test)
        #write into promql
        writeDataToDb(predictedData)
        return home()

@application.route('/build_lr_ml', methods=['POST'])
def buildLrModel():
    lrmodel = buildLinearRegressionModel()
    saveModel(lrmodel)

if __name__ == "__main__":
    application.debug = True
    application.run()
#     dataFrame = getDatafromDb()
#     dataFrame = processDbDataForLrTestInput(dataFrame)
#     X_test, y_test = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
#     print(y_test)
#     predictedData = linearRegression(X_test)
#     print(predictedData)
#     writeDataToDb(predictedData)

