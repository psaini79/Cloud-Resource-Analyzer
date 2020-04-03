#!/usr/bin/env python

import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from database import  getDatafromDb
from predict import linearRegression


# for time-series cross-validation set 5 folds
tscv = TimeSeriesSplit(n_splits=5)


def timeseries_train_test_split(X, y, test_size):
    """
        Perform train-test split with respect to time series structure
    """

    # get the index after which test set starts
    test_index = int(len(X) * (1 - test_size))

    X_train = X.iloc[:test_index]
    y_train = y.iloc[:test_index]
    X_test = X.iloc[test_index:]
    y_test = y.iloc[test_index:]

    return X_train, X_test, y_train, y_test

def code_mean(data, cat_feature, real_feature):
    """
    Returns a dictionary where keys are unique categories
    and values are means
    """
    return dict(data.groupby(cat_feature)[real_feature].mean())

def prepareData(series, lag_start, lag_end, test_size, target_encoding=False):
    """
        series: pd.DataFrame
            dataframe with timeseries
        lag_start: int
            initial step back in time to slice target variable
            example - lag_start = 1 means that the model
                      will see yesterday's values to predict today
        lag_end: int
            final step back in time to slice target variable
            example - lag_end = 4 means that the model
                      will see up to 4 days back in time to predict today
        test_size: float
            size of the test dataset after train/test split as percentage of dataset
        target_encoding: boolean
            if True - add target averages to the dataset

    """
    # copy of the initial dataset
    data = pd.DataFrame(series.copy())
    data.columns = ["y"]

    # lags of series
    for i in range(lag_start, lag_end):
        data["lag_{}".format(i)] = data.y.shift(i)

    # datetime features
    data["hour"] = data.index.hour
    data["weekday"] = data.index.weekday
    # other features
    #data['network received'] = hourlydat[['Network received throughput [KB/s]']]
    #data['network transmitted'] = hourlydat[['Network transmitted throughput [KB/s]']]
    #data['cpu diff'] = hourlydat[['CPU_diff']]
    #data['received_prev'] = hourlydat[['received_prev']]
    #data['core'] = hourlydat[['CPU cores']]

    if target_encoding:
        # calculate averages on train set only
        test_index = int(len(data.dropna()) * (1 - test_size))
        data['weekday_average'] = list(map(
            code_mean(data[:test_index], 'weekday', "y").get, data.weekday))
        data["hour_average"] = list(map(
            code_mean(data[:test_index], 'hour', "y").get, data.hour))

        # drop encoded variables
        data.drop(["hour", "weekday"], axis=1, inplace=True)

    # train-test split
    y = data.dropna().y
    X = data.dropna().drop(['y'], axis=1)
    #X_train, X_test, y_train, y_test = timeseries_train_test_split(X, y, test_size=test_size)

    #return X_train, X_test, y_train, y_test
    return X, y


def processDbDataForLrTestInput(dataframe):
    dataframe = dataframe.drop(columns="system")
    dataframe = dataframe.drop(columns="user")
    dataframe = dataframe.drop(columns="iowait")
    dataframe = dataframe.drop(columns="irq")
    dataframe = dataframe.drop(columns="nice")
    dataframe = dataframe.drop(columns="softirq")
    dataframe = dataframe.drop(columns="steal")
    dataframe = dataframe.drop(columns="idle")
    dataframe['weekday'] = dataframe['time'].dt.dayofweek
    dataframe['weekend'] = ((dataframe.weekday) // 5 == 1).astype(float)
    dataframe['month'] = dataframe.time.dt.month
    dataframe['day'] = dataframe.time.dt.day
    dataframe.set_index('time', inplace=True)
    dataframe = dataframe.fillna(method='ffill')
    return dataframe


if __name__ == "__main__":
    dataFrame = getDatafromDb()
    dataFrame = processDbDataForLrTestInput(dataFrame)
    #print(dataFrame)
    hourlydat = dataFrame.resample('H').sum()
    #print(hourlydat)
    #print(dataFrame.CpuUsage.dtype)
    X_test, y_train = \
        prepareData(hourlydat[['CpuUsage']], lag_start=3, lag_end=10, test_size=.9, target_encoding=True)
    print(X_test)
    predict = linearRegression(X_test)
    print(predict)
