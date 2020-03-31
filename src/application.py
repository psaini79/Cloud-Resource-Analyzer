#!flask/bin/python
import os
import json

from flask import Flask
from flask import request
from settings import SECRET_KEY
from predict import linearRegression

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
        tenantname = request.form['tenant_name']
        #period = request.form['period']
        xtest = {} #read from promql
        predicted_data = linearRegression(xtest)
        #write into promql
        return home()


if __name__ == "__main__":
    application.debug = True 
    application.run()
