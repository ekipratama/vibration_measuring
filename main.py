import readWriteData as rwd
# import SensorData as sensor
import PlotData as plt
import fourierTransform as ft
import numpy as np
from scipy.signal import find_peaks


# def sampling():
#     x, y = sensor.sampleData()
#     sampledData = np.array([x, y])
#     rwd.saveToNpy(sampledData, "vibration_1500rpm_left_bearing_cycletime_200_unbalance_1_magneet.npy")
#     rwd.saveToCsv(sampledData, "vibration_1500rpm_left_bearing_cycletime_200_unbalance_1_magneet.csv")

# readedData = rwd.loadNpy("vibration_50hz_left_bearing_cycletime_10_unbalance.npy")
# readedData2 = rwd.loadNpy("vibration_50hz_left_bearing_cycletime_10_normal.npy")

# xTime = readedData[0]
# yTime = readedData[1]
# xTime2 = readedData2[0]
# yTime2 = readedData2[1]

# Test
# readedData = rwd.loadNpy("samples/vibration_1500rpm_left_bearing_cycletime_200_normal.npy")
# xTime = readedData[0]
# yTime = readedData[1]
# xFreq, yFreq = ft.calculateFourier(xTime, yTime)
# plt.plotGraph(xTime, yTime, xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)))

# Test Arduino

yTime = []

sample_rate = 2000
data_point = 8192
duration = data_point/sample_rate
with open('samples/arduino_1500rpm_unbalance_8192s.txt', 'r') as file:
    for line in file:
        yTime.append(float(line))

xTime = np.arange(0, duration, duration/data_point)


fourierTransform = np.fft.fft(yTime)/len(yTime)
fourierTransform = np.fft.fft(yTime)
fourierTransform = fourierTransform[range(int(len(yTime)/2))]
samplingFrequency = data_point/duration
tpCount = len(yTime)
values = np.arange(int(tpCount/2))
timePeriod = tpCount/samplingFrequency
frequencies = values/timePeriod
fourierTransform[0] = 0

plt.plotGraph(xTime, yTime, frequencies, np.abs(fourierTransform))

# Test arduino 3d

# yTime = []
# yTime2 = []
# sample_rate = 2000
# data_point = 4096
# duration = data_point/sample_rate
# with open('samples/arduino_1500rpm_normal_4096s.txt', 'r') as file:
#     for line in file:
#         yTime.append(float(line))

# with open('samples/arduino_1500rpm_unbalance_4096s.txt', 'r') as file2:
#     for line in file2:
#         yTime2.append(float(line))

# xTime = np.arange(0, 2.048, 0.0005) # 2000 hz
# xTime2 = np.arange(0, 2.048, 0.0005) # 2000 hz

# fourierTransform = np.fft.fft(yTime)/len(yTime)
# fourierTransform = np.fft.fft(yTime)
# fourierTransform = fourierTransform[range(int(len(yTime)/2))]
# samplingFrequency = data_point/duration
# tpCount = len(yTime)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/samplingFrequency
# frequencies = values/timePeriod
# fourierTransform[0] = 0
# print(frequencies)

# fourierTransform2 = np.fft.fft(yTime2)/len(yTime2)
# fourierTransform2 = np.fft.fft(yTime2)
# fourierTransform2 = fourierTransform2[range(int(len(yTime2)/2))]
# samplingFrequency2 = data_point/duration
# tpCount2 = len(yTime2)
# values2 = np.arange(int(tpCount2/2))
# timePeriod2 = tpCount2/samplingFrequency2
# frequencies2 = values2/timePeriod2
# fourierTransform2[0] = 0

# plt.compare2Data3d(frequencies, fourierTransform, frequencies2, fourierTransform2)



# Test Esp32
# xTime = []
# yTime = []
# with open('samples/samples_1500rpm_normal_sensor_ifm_sp_10k_left_bearing.txt', 'r') as file:
#     for line in file:
#         # Extract x and y values from each line
#         x, y = line.strip().split(',')
#         x = float(x)
#         y = float(y)

#         # Append the values to the samples list
#         xTime.append(x)
#         yTime.append(y)

# xTime = np.linspace(0, max(xTime), max(xTime)/len(yTime))
# yTime = yTime
# #fourierTransform = np.fft.fft(yTime)/len(yTime)
# fourierTransform = np.fft.fft(yTime)
# fourierTransform = fourierTransform[range(int(len(yTime)/2))]
# samplingFrequency = len(yTime)/max(xTime)
# tpCount = len(yTime)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/samplingFrequency
# frequencies = values/timePeriod
# fourierTransform[0] = 0

# plt.plotGraph(xTime, yTime, frequencies, np.abs(fourierTransform))


# Test rberry pi pico data

# txtfile=open('samples/1500rpm_unbalance.txt').read()
# yTime = [int(x) for x in txtfile.strip("[]").split(",")]
# print(len(yTime))
# xTime = np.arange(0, 3000, 1/2)


# # xFreq, yFreq = ft.calculateFourier(xTime, yTime)
# # plt.plotGraph(xTime, yTime, xFreq[1:], 2*np.abs((yFreq[1:]/(len(yFreq[1:])/2))))
# lowx, lowy = ft.addLowFilter(xTime, yTime)
# fourierTransform = np.fft.fft(lowy)/len(lowy)
# fourierTransform = fourierTransform[range(int(len(lowy)/2))]
# samplingFrequency = 2000
# tpCount = len(lowy)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/samplingFrequency
# frequencies = values/timePeriod
# frequencies[np.argmax(np.abs(fourierTransform))]
# frequencies[0] = 0
# plt.plotGraph(lowx, lowy, frequencies, np.abs(fourierTransform))


# Test np
# readedData = rwd.loadNpy("samples/vibration_1500hz_left_bearing_cycletime_200.npy")
# xTime = readedData[0]
# yTime = readedData[1]
# fourierTransform = np.fft.fft(yTime)/len(yTime)
# fourierTransform = fourierTransform[range(int(len(yTime)/2))]

# samplingFrequency = 4
# tpCount = len(yTime)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/samplingFrequency
# frequencies = values/timePeriod
# plt.plotGraph(xTime, yTime, frequencies, np.abs(fourierTransform))

# Test 1.1
# readedData = rwd.loadNpy("vibration_50hz_left_bearing_cycletime_200.npy")
# xTime = readedData[0]
# yTime = readedData[1]
# xFreq, yFreq = ft.calculateFourier(xTime, yTime)
# plt.plotGraph(xTime, yTime, xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)))

# Test 1.2
# readedData = rwd.loadNpy("vibration_50hz_left_bearing_cycletime_200.npy")
# xTime = readedData[0]
# yTime = readedData[1]
# xFreq, yFreq = ft.calculateFourier(xTime, yTime)
# plt.plotGraph(xTime, yTime, xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)))

# Test 1.3
# readedData = rwd.loadNpy("vibration_50hz_left_bearing_cycletime_10_normal.npy")
# xTime = readedData[0]
# yTime = readedData[1]
# xFreq, yFreq = ft.calculateFourier(xTime, yTime)
# plt.plotGraph(xTime, yTime, xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)))

# Test 2.1
# readedData = rwd.loadNpy("vibration_500rpm_left_bearing_cycletime_200_normal.npy")
# readedData2 = rwd.loadNpy("vibration_1000rpm_left_bearing_cycletime_200_normal.npy")
# readedData3 = rwd.loadNpy("vibration_1500rpm_left_bearing_cycletime_200_normal.npy")

# xTime = readedData[0]
# yTime = readedData[1]
# xTime2 = readedData2[0]
# yTime2 = readedData2[1]
# xTime3 = readedData3[0]
# yTime3 = readedData3[1]

# xFreq, yFreq = ft.calculateFourier(xTime, yTime)
# xFreq2, yFreq2 = ft.calculateFourier(xTime2, yTime2)
# xFreq3, yFreq3 = ft.calculateFourier(xTime3, yTime3)
# plt.compare3Data(
#     xTime, yTime,
#     xTime2, yTime2, 
#     xTime3, yTime3, 
#     xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)), 
#     xFreq2[1:], 2*np.abs(yFreq2[1:])/(len(yFreq2[1:]/2)), 
#     xFreq3[1:], 2*np.abs(yFreq3[1:])/(len(yFreq3[1:]/2)))

# Test 2.2
# readedData = rwd.loadNpy("samples/vibration_500rpm_left_bearing_cycletime_200_normal.npy")
# readedData2 = rwd.loadNpy("samples/vibration_1000rpm_left_bearing_cycletime_200_normal.npy")
# readedData3 = rwd.loadNpy("samples/vibration_1500rpm_left_bearing_cycletime_200_normal.npy")

# xTime = readedData[0][:256]
# yTime = readedData[1][:256]
# xTime2 = readedData2[0][:256]
# yTime2 = readedData2[1][:256]
# xTime3 = readedData3[0][:256]
# yTime3 = readedData3[1][:256]
# print(xTime)
# xFreq, yFreq = ft.calculateFourier(xTime, yTime)
# xFreq2, yFreq2 = ft.calculateFourier(xTime2, yTime2)
# xFreq3, yFreq3 = ft.calculateFourier(xTime3, yTime3)

# plt.compare3Data(
#     xTime, yTime,
#     xTime2, yTime2, 
#     xTime3, yTime3, 
#     xFreq[1:], np.abs(yFreq[1:]), 
#     xFreq2[1:], np.abs(yFreq2[1:]), 
#     xFreq3[1:], np.abs(yFreq3[1:]))

# Test 3.1
# readedData = rwd.loadNpy("vibration_1500rpm_left_bearing_cycletime_200_normal.npy")
# readedData2 = rwd.loadNpy("vibration_1500rpm_left_bearing_cycletime_200_unbalance_1_magneet.npy")
# readedData3 = rwd.loadNpy("vibration_1500rpm_left_bearing_cycletime_200_unbalance_2_magneet.npy")


# xTime = readedData[0][:256]
# yTime = readedData[1][:256]
# xTime2 = readedData2[0][:256]
# yTime2 = readedData2[1][:256]
# xTime3 = readedData3[0][:256]
# yTime3 = readedData3[1][:256]


# xFreq, yFreq = ft.calculateFourier(xTime, yTime)
# xFreq2, yFreq2 = ft.calculateFourier(xTime2, yTime2)
# xFreq3, yFreq3 = ft.calculateFourier(xTime3, yTime3)


# plt.compare4Data(
#     xTime, yTime,
#     xTime2, yTime2, 
#     xTime3, yTime3,  
#     xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)), 
#     xFreq2[1:], 2*np.abs(yFreq2[1:])/(len(yFreq2[1:]/2)), 
#     xFreq3[1:], 2*np.abs(yFreq3[1:])/(len(yFreq3[1:]/2)))

# xFreq2, yFreq2 = ft.calculateFourier(xTime2, yTime2)
# plt.compare2Data(xTime, yTime, xTime2, yTime2, xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)), xFreq2[1:], 2*np.abs(yFreq2[1:])/(len(yFreq2[1:]/2)))

# sampling()

#plt.plotGraph(xTime, yTime, xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)))
# xFil, yFil = ft.addLowFilter(xTime, yTime)

#plt.plot2(xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)), xFreq2[1:], 2*np.abs(yFreq2[1:])/(len(yFreq2[1:]/2)))

