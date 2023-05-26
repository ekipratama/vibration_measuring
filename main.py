import readWriteData
import SensorData
import PlotData
import fourierTransform

def sampling():
    x, y = sampleData()
    sampledData = np.array([x, y])
    saveToNpy(sampledData, "sampledData.npy")


readedData = loadNpy("sampledData.npy")
xTime = readedData[0]
yTime = readedData[1]
xFreq, yFreq = calculateFourier(xTime, yTime)
plotGraph(xTime, yTime, xFreq[1:], 2*np.abs(yFreq[1:])/(len(yFreq[1:]/2)))

