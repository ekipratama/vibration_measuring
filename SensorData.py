import revpimodio2
import numpy as np
from pathlib import Path

xSample = []
ySample = []

sampleRate = 4096
cycleTime = 10
readMode = True

rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)
rpi.handlesignalend()


    
def read():
    return rpi.io.AIn_2.value
    

def readRawData():
    rawData = Path('/sys/bus/iio/devices/iio:device1/in_voltage1_raw').read_text()
    dataInMv = ((int (rawData) * 12500) >> 21) + 6250
    

def writeToText(items):
    
    np.savetxt('item.csv', items, delimiter = " ", fmt = '% s ')


def addDataToSample(cycletools):
    data = read()
    if not readMode:
        data = readRawData()
        
    if len(ySample) == sampleRate:
        xSample = np.arange(0, cycleTime * sampleRate/1000, cycleTime/1000)
        rpi.exit()
        print("Done sampeling")
        return xSample, ySample
    ySample.append(data)
    

def sampleData():
    print("sampeling data...")
    sample, sample1 = rpi.cycleloop(addDataToSample, cycleTime)
    
    return sample, sample1


