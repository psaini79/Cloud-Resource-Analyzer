
import settings
from multiprocessing import Process
from predict import linearRegression
from predict import randomForest 
from database import getDatafromDb, writeDataToDb
from models import *
from dataprocessor import *

class processPrediction:
    pName = None
    def __init__(self, period, model):
        p = Process(target=self.run, args=(period,model,))
        p.daemon = True                       # Daemonize it
        p.start()                             # Start the execution
        self.pName = p

    def run(self, period, mlName):
        print("starting prediction for "+period+" days"+ " with "+mlName)
        dataFrame = getDatafromDb(period)
        print(dataFrame)
        dataFrame = processDbDataForLrTestInput(dataFrame)
        X_test, y_test = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
        print("y_test")
        print(y_test)
        if(mlName == "LR"):
            predictedData = linearRegression(X_test)
        elif(mlName == "RF"):
            predictedData = randomForest(X_test)
        else:
            print("Invalid Model"+ mlName)
            return
        # write into promql
        writeDataToDb(predictedData)
        print("predicted")
        print(predictedData)
        print(mlName + " Model completed prediction for "+ period)

    def getStatus(self):
        return self.pName.is_alive()


class processModelBuild:

    def __init__(self, model):
         p = Process(target=self.run, args=(model,))
         p.daemon = True  # Daemonize it
         p.start()  # Start the execution

    def run(self, mlName):
        print("Building Model ", mlName)
        if(mlName == "LR"):
            model = buildLinearRegressionModel()
            name = settings.ML_LR_MODEL
        elif(mlName == "RF"):
            model = buildRandomForestMNodel()
            name =  settings.ML_RF_MODEL
        else:
            print("Invalid Building Model", mlName, "completed")
            return
        saveModel(model, name)
        print("Building Model", mlName, "completed")


if __name__ == "__main__":
    dataFrame = getDatafromDb(1)
    dataFrame = processDbDataForLrTestInput(dataFrame)
    print(dataFrame)
    X_test, y_test = prepareData(dataFrame[['CpuUsage']], lag_start=3, lag_end=25)
    predictedData = linearRegression(X_test)
    print(y_test)
    print(predictedData)
    error = mean_absolute_percentage_error(predictedData, y_test)
    print("Mean Absolute Error: {0:.2f}%".format(error))
