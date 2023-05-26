import matplotlib.pyplot as plt
import numpy as np
import SensorData
from scipy.fftpack import rfft, rfftfreq

def plotGraph(x1Data, y1Data, x2Data, y2Data):
    
    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Velocity (mm/s)')
    
    axs[0].plot(x1Data, y1Data)
    axs[1].plot(x2Data, y2Data)
    fig.tight_layout()
    plt.show()
    
x1, y1 = SensorData.sampleData()
y2 = rfft(y1)
x2 = rfftfreq(len(y2), 1/2000)


