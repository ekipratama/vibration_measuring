#from scipy.fftpack import rfft, rfftfreq
from scipy.fft import rfft, rfftfreq
import scipy.signal

def calculateFourier(xData, yData):
    yFreq = rfft(yData)
    xFreq = rfftfreq(len(yData), 1/(len(yData)/max(xData)))
    # xFreq = rfftfreq(len(yData), 1/10)
    return xFreq, yFreq

def addLowFilter(xData, yData):
    b, a = scipy.signal.iirfilter(4, Wn=0.2, btype="low", ftype="butter")
    y_Ifilter = scipy.signal.lfilter(b, a, yData)
    
    return xData, y_Ifilter