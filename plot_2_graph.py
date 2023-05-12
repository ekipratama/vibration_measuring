import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import revpimodio2
from scipy.fftpack import rfft, rfftfreq
from pathlib import Path

# create new instance of revpimodio2 in readonly (monitoring) mode
rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)

# catch SIGINT and handle proper release of all IOs
rpi.handlesignalend()
rpi.cycletime = 50

def data_gen():
    t = data_gen.t
    cnt = 0
    while cnt < 1000:
        sensorData = Path('/sys/bus/iio/devices/iio:device1/in_voltage1_raw').read_text()
        volt = ((int (sensorData) * 12500) >> 21) + 6250
        cnt+=1
        t += 1
        y1 = volt
        print(y1)
        yield t, y1

data_gen.t = 0

# create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2,1)

# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')
line = [line1, line2]

# the same axes initalizations as before (just now we do it for both of them)

ax1.set_ylim(1500, 3000)
ax1.set_xlim(0, 100)
ax1.grid()
ax1.set_xlabel('samples')
ax1.set_ylabel('Voltage')

ax2.set_ylim(-1000, 1000) 
ax2.set_xlim(0, 1000)
ax2.grid()
ax2.set_xlabel('frequenties')
ax2.set_ylabel('amplitudes')

# initialize the data arrays 
x1data, x2data, y1data, y2data = [], [], [], []

def run(data):
    # update the data
    t, y1 = data
    x1data.append(t)
    y1data.append(y1)
    y2data = rfft(y1data)/len(y1data)
    x2data = rfftfreq(len(y2data), 1/1000)

    # axis limits checking. Same as before, just for both axes
    
    xmin, xmax = ax1.get_xlim()
    if t >= xmax:
        ax1.set_xlim(xmin, 2*xmax)
        ax1.figure.canvas.draw()

    # update the data of both line objects
    line[0].set_data(x1data, y1data)
    line[1].set_data(x2data, y2data)

    return line

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=50 ,
    repeat=False)
plt.show()