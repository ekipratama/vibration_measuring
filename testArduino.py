
import readWriteData as rwd
import PlotData as plt
import numpy as np

# Test 1.1
# yTime = []

# sample_rate = 2000
# data_point = 4096
# duration = data_point/sample_rate
# with open('samples/arduino_1500rpm_normal_4096s.txt', 'r') as file:
#     for line in file:
#         velocity = ((float(line) - 180) / (901 - 180)) * 25
#         yTime.append(velocity*4)

# xTime = np.arange(0, duration, duration/data_point)

# fourierTransform = np.fft.fft(yTime)/len(yTime)
# fourierTransform = np.fft.fft(yTime)
# fourierTransform = fourierTransform[range(int(len(yTime)/2))]
# samplingFrequency = data_point/duration
# tpCount = len(yTime)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/samplingFrequency
# frequencies = values/timePeriod
# fourierTransform[0] = 0

# plt.plotGraphArduino(xTime, yTime, frequencies, np.abs(fourierTransform), showPeak=True)

# Test 1.2

yTime = []

sample_rate = 2000
data_point = 4096
duration = data_point/sample_rate
with open('samples/arduino_1500rpm_unbalance2_4096s.txt', 'r') as file:
    for line in file:
        velocity = ((float(line) - 180) / (901 - 180)) * 25
        yTime.append(velocity*4)

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

plt.plotGraphArduino2(xTime, yTime, frequencies, np.abs(fourierTransform), showPeak=True)

# Test 1.3

yTime = []

sample_rate = 2000
data_point = 4096
duration = data_point/sample_rate
with open('samples/arduino_1500rpm_unbalance2_4096s.txt', 'r') as file:
    for line in file:
        velocity = ((float(line) - 180) / (901 - 180)) * 25
        yTime.append(velocity*4)

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

plt.plotGraphArduino2(xTime, yTime, frequencies, np.abs(fourierTransform), showPeak=True)


# Test 2

# yTime = []

# sample_rate = 2000
# data_point = 4096
# duration = data_point/sample_rate
# with open('samples/arduino_1500rpm_normal_4096s.txt', 'r') as file:
#     for line in file:
#         velocity = ((float(line) - 180) / (901 - 180)) * 25
#         yTime.append(velocity*4)

# xTime = np.arange(0, duration, duration/data_point)

# fourierTransform = np.fft.fft(yTime)/len(yTime)
# fourierTransform = np.fft.fft(yTime)
# fourierTransform = fourierTransform[range(int(len(yTime)/2))]
# samplingFrequency = data_point/duration
# tpCount = len(yTime)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/samplingFrequency
# frequencies = values/timePeriod
# fourierTransform[0] = 0

# plt.plotGraphArduino3(xTime, yTime, frequencies, np.abs(fourierTransform), showPeak=True)
