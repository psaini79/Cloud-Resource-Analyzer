#!flask/bin/python
import json
import settings 

from flask import Flask
from flask import request
from Process import processPrediction
from Process import processModelBuild


application = Flask(__name__)
application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 
application.config['SESSION_TYPE'] = settings.SECRET_KEY

@application.route('/')
def home():
   print("This is CRA ML Analyser")
   return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@application.route('/trigger_ml', methods=['POST'])
def triggerML():
    error = None
    if request.method == 'POST':
        period = request.form['period']
        try:
            processPrediction(period)
        except:
            return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}
        return json.dumps({'Inprogress': True}), 200, {'ContentType': 'application/json'}


@application.route('/build_ml', methods=['POST'])
def buildLrModel():
    if request.method == 'POST':
        model = request.form['model']
    try:
        processModelBuild(model)
    except:
        return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}
    return json.dumps({'Inprogress': True}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    application.debug = settings.DEBUG 
    application.run(host="0.0.0.0", port="5000")
#     dataFrame = getDatafromDb()
#     dataFrame = processDbDataForLrTestInput(dataFrame)
#     X_test, y_test = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
#     print(y_test)
#     predictedData = linearRegression(X_test)
#     print(predictedData)
#     writeDataToDb(predictedData)

