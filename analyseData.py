import Sensordata as sd

def peakValue(lowestValue, highestValue, currentValue):
    maxAmplitude = highestValue - lowestValue
    
    if maxAmplitude < currentValue:
        return maxAmplitude
    else:
        return currentValue
    
    