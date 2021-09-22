import csv
import datetime
import time
import os
from random import seed
from random import randint


def runDataProcessing():
    count = 0
    while True:
        count = count + 1
        #define all names and dates
        x = datetime.datetime.now()
        folderDate = x.strftime("%m-%b-%Y")
        fileDate = x.strftime("%d-%b-%Y")
        writeTime = x.strftime("%d-%m %H:%M")
        randomNumber = randint(0, 100)
        
        #wrapping all data in array
        sendOnce = ['OS', 'Datum', 'bericht nummer', 'random nummer']
        sendData = [os, fileDate, count, randomNumber]

        #sending array's
        with open(folderDate + "/" + fileDate + '.csv', 'w', encoding='UTF8', newline = '') as f:
            header = csv.writer(f)

        time.sleep(1)
        
        