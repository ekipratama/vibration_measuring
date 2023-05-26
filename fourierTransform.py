from scipy.fftpack import rfft, rfftfreq

def calculateFourier(xData, yData):
    yFreq = rfft(yData)
    xFreq = rfftfreq(len(yData), len(yData)/max(xData)/2)
    return xFreq, yFreq

