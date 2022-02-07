from genericpath import isdir, isfile
import csv
import datetime
import time
import os
from random import randint

count = 0
while True:
    #define all names and dates
    x = datetime.datetime.now()
    folderDate = x.strftime("%m-%b-%Y")
    fileDate = x.strftime("%d-%b-%Y")
    writeTime = x.strftime("%d-%m %H:%M")
    dirPath = '/static/excel-data/' + folderDate
    dataFile = f'/static/excel-data/{folderDate}/{fileDate}.csv'

    #Make fake test vals
    sendStuf = [2,0,0,1,3,4,0,0,1,3,4,0,0,1,3,4,0,0,1,3,4]
    deltaT = 0
    i = 0
    while i <= 20:
        if sendStuf[i] == 4:
            sendStuf[i] = randint(20, 200)
        elif sendStuf[i] == 3:
            sendStuf[i] = randint(1, 20)
        elif sendStuf[i] == 2:
            sendStuf[i] = writeTime
        elif sendStuf[i] == 1:
            if sendStuf[i-2] > sendStuf [i-1]:
                deltaT = sendStuf[i-2] - sendStuf[i-1]
            elif sendStuf[i-1] > sendStuf [i-2]:
                deltaT = sendStuf[i-1] - sendStuf[i-2]
            sendStuf[i] = deltaT
        elif sendStuf[i] == 0:
            sendStuf[i] = randint(18, 30)
        i = i + 1
    
    
    #wrapping all data in array
    sendOnce = ['Datum/tijd', 'T1', 'T2', 'Delta-1', 'Flow-1', 'Power-1', 'T3', 'T4', 'Delta-2', 'Flow-2', 'Power-2', 'T5', 'T6', 'Delta-3', 'Flow-3', 'Power-3', 'T7', 'T8', 'Delta-4', 'Flow-H2', 'Power-H2']
    sendData = [writeTime, sendStuf]

    if not isdir(dirPath):
        os.makedirs(dirPath)

    elif isdir(dirPath):
        if not isfile(dataFile):
            with open(dataFile, 'w', encoding='UTF8', newline = '') as f:
                header = csv.writer(f)
                header.writerow(sendOnce)

        elif isfile(dataFile):
            with open(dataFile, 'a', encoding='UTF8', newline = '') as f:
                data = csv.writer(f)
                data.writerow(sendStuf)
            time.sleep(1)