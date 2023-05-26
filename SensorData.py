import revpimodio2
import numpy as np
from pathlib import Path

xSample = np.array([])
ySample = np.array([])

sampleRate = 4096
cycleTime = 10
readMode = True

rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)
rpi.handlesignalend()


def voltToVelocity(volt):
    velocity = ((volt - 1880)/8120) * 25
    return velocity

def read():
    return voltToVelocity(rpi.io.AIn_2.value)
    

def readRawData():
    rawData = Path('/sys/bus/iio/devices/iio:device1/in_voltage1_raw').read_text()
    dataInMv = ((int (rawData) * 12500) >> 21) + 6250

    return voltToVelocity(dataInMv)
    

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
    

def sampleData(sample_rate = 4096, cycle_time = 10):
    global sampleRate
    global cycleTime
    sampleRate = sample_rate
    cycleTime = cycle_time
    print("sampeling data...")
    sample, sample1 = rpi.cycleloop(addDataToSample, cycleTime)
    
    return sample, sample1


