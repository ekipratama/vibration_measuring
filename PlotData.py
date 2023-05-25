import matplotlib.pyplot as plt
import numpy as np
import SensorData
from scipy.fftpack import rfft, rfftfreq

def plotGraph(x1Data, y1Data, x2Data, y2Data):
    
    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Voltage (mV)')
    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Voltage (mV)')
    
    axs[0].plot(x1Data, y1Data)
    axs[1].plot(x2Data, y2Data)
    plt.show()
    
x1, y1 = SensorData.sampleData()
y2 = rfft(y1)
x2 = rfftfreq(len(y2), 1/2000)
plotGraph(x1, y1, x2[1:], 2*np.abs(y2[1:])/(len(y2[1:]/2)))

