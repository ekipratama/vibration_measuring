import readWriteData as rwd
import SensorData as sensor
import PlotData as plt
import fourierTransform as ft
import numpy as np


def sampling():
    x, y = sensor.sampleData()
    sampledData = np.array([x, y])
    rwd.saveToNpy(sampledData, "vibration_10hz_left_bearing_cycletime_200.npy")
    rwd.saveToCsv(sampledData, "vibration_10hz_left_bearing_cycletime_200.csv")

readedData = rwd.loadNpy("vibration_10hz_left_bearing_cycletime_200.npy")
readedData2 = rwd.loadNpy("vibration_50hz_left_bearing_cycletime_200.npy")

xTime = readedData[0]
yTime = readedData[1]
xTime2 = readedData2[0]
yTime2 = readedData2[1]

xFreq, yFreq = ft.calculateFourier(xTime, yTime)
xFreq2, yFreq2 = ft.calculateFourier(xTime2, yTime2)
# xFil, yFil = ft.addLowFilter(xTime, yTime)
plt.plot2(xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)), xFreq2[1:], 2*np.abs(yFreq2[1:])/(len(yFreq2[1:]/2)))
# plt.plotGraph(xFil, yFil, xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)))

#sampling()
