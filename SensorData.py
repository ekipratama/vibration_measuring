import revpimodio2
import numpy as np
from pathlib import Path

xSample = []
ySample = []

sampleRate = 1024
cycleTime = 200
readMode = False

rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)
rpi.handlesignalend()
raw = open('/sys/bus/iio/devices/iio:device1/in_voltage1_raw', 'r')


def voltToVelocity(volt):
    velocity = ((volt - 1880)/8120) * 25
    return velocity

def read():
    return round(voltToVelocity(rpi.io.AIn_2.value), 2)
    

def readRawData():
    raw.seek(0)
    rawData = raw.read()
    dataInMv = ((int (rawData) * 12500) >> 21) + 6250

    return round(np.abs(voltToVelocity(dataInMv)), 2)
    

def addDataToSample(cycletools):
    data = read()
    if not readMode:
        data = readRawData()
        
    if len(ySample) == sampleRate:
        xSample = np.arange(0, (cycleTime * sampleRate)/1000, cycleTime/1000)
        rpi.exit()
        print("Done sampeling")
        return xSample, ySample
    ySample.append(data)
    
    

def sampleData():
    
    print("sampeling data...")
    sample, sample1 = rpi.cycleloop(addDataToSample, cycleTime)
    
    return sample, sample1


