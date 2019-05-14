author = "Sagar Patel"
'''
The goal is to use machine learning and the summon data that I have collected
over the past few months. Add it with the data collected from other users and
then I should be able to predict when is a good time to summon for a certain unit
It should be accurate in that it gives me the best possibble time to summon.
I am hoping for above 70% accuracy rate.
'''

#import statements
import pandas as pd
import quandl
import math, datetime
import numpy as np
from decimal import Decimal
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

print("Welcome to Dokkan Selector")
debug = True

def debugMessage(message):
    if(debug):
        print(message)



debugMessage("Dokkan Selector Started")

class DokkanSummons():
    def __init__(self):
        print("Dokkan Summons Class Created")
        self.dayList = []
        self.timeList = []
        self.fDayList = []
        self.fTimeList = []
        self.minList = []
        self.dList = []
        self.fDlist = []
        self.fMinList = []
        self.Friday = []
        self.Saturday = []
        self.Sunday = []
        self.pltFigure = plt.figure()
        self.pltAxes = self.pltFigure.add_subplot(111)

    def createPlot(self):
        debugMessage("createPlot: Creating Plot")
        dataFile = open("SummonData.txt","r")
        x = []
        rawData = []
        y = []
        print("Check Point")
        for line in dataFile:
            rawData.append(line.split())
        for i in rawData:
            print(i)
            self.processData(i)
        print(self.timeList)
        print(self.dayList)
        x = self.dayList
        y = self.timeList
        print(x)
        print(y)
        self.pltAxes.scatter(x,y,s=20,c='blue',marker="*")
        self.pltAxes.scatter(self.fDayList,self.fTimeList,s=20,c='red',marker="+")
        #https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
        #URL to plot multiple datasets
        plt.show()
        '''
        String Layout: S Featured Rarity Day Hr min sec
        '''
    def processData(self,dataList):
        print("processData: Checkpoint A")
        result = []
        isFeatured = False
        if dataList[1] == "Featured":
            isFeatured = True
        else:
            isFeatured = False
        temp = dataList[4].split(":")
        hr = float(temp[1])
        temp = dataList[5].split(":")
        min = float(temp[1])
        temp = dataList[6].split(":")
        sec = float(temp[1])
        min = min/60.0
        sec = sec/(60.0*60.0)
        time = hr + min + sec
        print(time)
        if isFeatured:
            if "SSR" in dataList:
                if "Sunday" in dataList:
                    self.fDayList.append(1)
                elif "Monday" in dataList:
                    self.fDayList.append(2)
                elif "Tuesday" in dataList:
                    self.fDayList.append(3)
                elif "Wednesday" in dataList:
                    self.fDayList.append(4)
                elif "Thursday" in dataList:
                    self.fDayList.append(5)
                elif "Friday" in dataList:
                    self.fDayList.append(6)
                elif "Saturday" in dataList:
                    self.fDayList.append(7)
                self.fTimeList.append(time)
        else:
            if "SSR" in dataList:
                if "Sunday" in dataList:
                    self.dayList.append(1)
                elif "Monday" in dataList:
                    self.dayList.append(2)
                elif "Tuesday" in dataList:
                    self.dayList.append(3)
                elif "Wednesday" in dataList:
                    self.dayList.append(4)
                elif "Thursday" in dataList:
                    self.dayList.append(5)
                elif "Friday" in dataList:
                    self.dayList.append(6)
                elif "Saturday" in dataList:
                    self.dayList.append(7)
                self.timeList.append(time)
        return result

    # SHows how many units Pulled per minute by date
    def minPulled(self):
        dataFile = open("SummonData.txt","r")
        x = []
        rawData = []
        y = []
        print("Check Point")
        for line in dataFile:
            rawData.append(line.split())
        for i in rawData:
            print(i)
            self.processMinData(i)
            print(i)
        print(self.minList)
        print(self.dayList)
        x = self.dayList
        y = self.minList
        print(x)
        print(y)
        self.pltAxes.scatter(self.dayList,self.minList,s=20,c='blue',marker="*")
        self.pltAxes.scatter(self.fDayList,self.fMinList,s=20,c='red',marker="+")
        #https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
        #URL to plot multiple datasets
        plt.show()

    def processMinData(self,dataList):
        print("process Minute Data")
        isFeatured = False
        if dataList[1] == "Featured":
            isFeatured = True
        else:
            isFeatured = False
        temp = dataList[5].split(":")
        min = float(temp[1])
        temp = dataList[6].split(":")
        sec = float(temp[1])
        sec = sec/(60.0)
        min = min + sec
        if isFeatured or ("SSR" in dataList):
            self.fMinList.append(min)
            if "Sunday" in dataList:
                self.fDayList.append(1)
            elif "Monday" in dataList:
                self.fDayList.append(2)
            elif "Tuesday" in dataList:
                self.fDayList.append(3)
            elif "Wednesday" in dataList:
                self.fDayList.append(4)
            elif "Thursday" in dataList:
                self.fDayList.append(5)
            elif "Friday" in dataList:
                self.fDayList.append(6)
            elif "Saturday" in dataList:
                self.fDayList.append(7)
        elif "SSR" in dataList:
            self.minList.append(min)
            if "Sunday" in dataList:
                self.dayList.append(1)
            elif "Monday" in dataList:
                self.dayList.append(2)
            elif "Tuesday" in dataList:
                self.dayList.append(3)
            elif "Wednesday" in dataList:
                self.dayList.append(4)
            elif "Thursday" in dataList:
                self.dayList.append(5)
            elif "Friday" in dataList:
                self.dayList.append(6)
            elif "Saturday" in dataList:
                self.dayList.append(7)
        print(min)
        print("End")




    def prediction(self):
        debugMessage("prediction: Predicting Summons")
        debugMessage("prediction: Function in Development")

    def insertSummonData(self,summonData):
        dataFile = open("SummonData.txt","a")
        dataFile.write(summonData)
        dataFile.close()
        debugMessage("insertSummonData: Inserting Summon Data")
        debugMessage("insertSummonData: Function in Development")

'''
Parameters:
Number of Cards in the Banner
Time
GSSR, Double Rates, Normal Rates
#of SSR's on the banner vs # of Featured SSR on the Banner
'''
