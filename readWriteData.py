import numpy as np

# filename has to end with .npy
def saveToNpy(data, fileName):
    np.save(fileName, data)

def loadNpy(fileName):
    data = np.load(fileName)
    return data

# format:
# signed int = %d
# unsigned int = %u
# float = %f
# see more at: https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html
def saveToCsv(data, fileName, format = "%.2f"):
    np.savetxt(fileName, data, fmt = format)

def loadCsv(fileName, dataType = int):
    data = np.loadtxt(fileName, dtype = dataType)
    return data
