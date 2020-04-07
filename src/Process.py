from multiprocessing import Process
from predict import linearRegression
from database import getDatafromDb, writeDataToDb
from models import buildLinearRegressionModel
from models import saveModel
from dataprocessor import processDbDataForLrTestInput
from dataprocessor import prepareData

class processPrediction:
    pName = None
    def __init__(self, period):
        p = Process(target=self.run, args=(period,))
        p.daemon = True                       # Daemonize it
        p.start()                             # Start the execution
        self.pName = p

    def run(self, period):
        print("starting prediction for "+period+" days")
        dataFrame = getDatafromDb(period)
        dataFrame = processDbDataForLrTestInput(dataFrame)
        X_test, y_test = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
        predictedData = linearRegression(X_test)
        # write into promql
        writeDataToDb(predictedData)
        print("completed prediction for "+ period)

    def getStatus(self):
        return self.pName.is_alive()


class processModelBuild:

    def __init__(self, model):
         p = Process(target=self.run, args=(model,))
         p.daemon = True  # Daemonize it
         p.start()  # Start the execution

    def run(self, model):
        lrmodel = buildLinearRegressionModel()
        saveModel(lrmodel)
