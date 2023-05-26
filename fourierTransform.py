from scipy.fftpack import rfft, rfftfreq
import scipy.signal

def calculateFourier(xData, yData):
    yFreq = rfft(yData)
    xFreq = rfftfreq(len(yData), 1/(len(yData)/max(xData)))
    return xFreq, yFreq

def addLowFilter(xData, yData):
    b, a = scipy.signal.iirfilter(4, Wn=0.9, btype="low", ftype="butter")
    y_Ifilter = scipy.signal.lfilter(b, a, yData)
    
    return xData, y_Ifilter