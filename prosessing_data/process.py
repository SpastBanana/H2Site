from genericpath import isdir, isfile
from H2Site import settings
import csv
import datetime
import time
import os
from random import randint

def processData():
    count = 0
    while True:
        #define all names and dates
        x = datetime.datetime.now()
        folderDate = x.strftime("%m-%b-%Y")
        fileDate = x.strftime("%d-%b-%Y")
        writeTime = x.strftime("%d-%m %H:%M")
        randomNumber = randint(0, 100)
        basedir = str(settings.BASE_DIR)
        dirPath = basedir + '/static/excel-data/' + folderDate
        dataFile = basedir + '/static/excel-data/' + folderDate + '/' + fileDate + '.csv'
        
        #wrapping all data in array
        sendOnce = ['Datum', 'bericht nummer', 'random nummer']
        sendData = [writeTime, count, randomNumber]

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
                    data.writerow(sendData)

        count = count + 1
        time.sleep(60)
        
        