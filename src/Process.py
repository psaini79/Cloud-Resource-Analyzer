
import settings
from multiprocessing import Process
from predict import linearRegression
from database import getDatafromDb, writeDataToDb
from models import *
from dataprocessor import *

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

    def run(self, mlName):
        print("Building Model ", mlName)
        if(mlName == "lr"):
            model = buildLinearRegressionModel()
            name = settings.ML_LR_MODEL
        elif(mlName == "rf"):
            model = buildRandomForestMNodel()
            name =  settings.ML_RF_MODEL
        saveModel(model, name)
        print("Building Model", mlName, "completed")


if __name__ == "__main__":
    dataFrame = getDatafromDb(1)
    dataFrame = processDbDataForLrTestInput(dataFrame)
    X_test, y_test = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
    predictedData = linearRegression(X_test)
    print(y_test)
    print(predictedData)
    error = mean_absolute_percentage_error(predictedData, y_test)
    print("Mean Absolute Error: {0:.2f}%".format(error))
