import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import revpimodio2
from scipy.fftpack import rfft, rfftfreq
from pathlib import Path
from time import time

# create new instance of revpimodio2 in readonly (monitoring) mode
rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)

# catch SIGINT and handle proper release of all IOs
rpi.handlesignalend()
rpi.cycletime = 200

def data_gen():
    t1 = time()  
    t = data_gen.t
    cnt = 0
    while cnt < 1000:
#         sensorData = Path('/sys/bus/iio/devices/iio:device1/in_voltage1_raw').read_text()
#         volt = ((int (sensorData) * 12500) >> 21) + 6250
        volt = rpi.io.AIn_2.value
        cnt+=1
        t += 1
        y1 = volt
        t2 = time()
        t_sec = t2-t1
        yield t, y1, t_sec

data_gen.t = 0

# create a figure with four subplots
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.set_figwidth(6)
fig.set_figheight(10)
fig.tight_layout()
# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')
line3, = ax3.plot([], [], lw=2, color='r')
line4, = ax4.plot([], [], lw=2)
line = [line1, line2, line3, line4]

# the same axes initalizations as before (just now we do it for both of them)

ax1.set_ylim(1500, 3000)
ax1.set_xlim(0, 100)
ax1.grid()
ax1.set_xlabel('samples')
ax1.set_ylabel('Voltage')

ax2.set_ylim(-25000, 40000) 
ax2.set_xlim(0, 1000)
ax2.grid()
ax2.set_xlabel('frequencies')
ax2.set_ylabel('amplitudes')

ax3.set_ylim(-2000, 3000) 
ax3.set_xlim(0, 1000)
ax3.grid()
ax3.set_xlabel('frequencies')
ax3.set_ylabel('amplitudes')

ax4.set_ylim(1500, 3000)
ax4.set_xlim(0, 100)
ax4.grid()
ax4.set_xlabel('time')
ax4.set_ylabel('Voltage')


# initialize the data arrays 
x1data, x2data, y1data, y2data, x4data = [], [], [], [], []

def run(data):
    # update the data
    t, y1, t_sec = data
    x1data.append(t)
    y1data.append(y1)
    y2data = rfft(y1data)
    x2data = rfftfreq(len(y2data), 1/2000)
    
    x4data.append(t_sec)
    # axis limits checking. Same as before, just for both axes
    
    xmin, xmax = ax1.get_xlim()
    if t >= xmax:
        ax1.set_xlim(xmin, 2*xmax)
        ax1.figure.canvas.draw()

    # update the data of both line objects
    line[0].set_data(x1data, y1data)
    line[1].set_data(x2data, y2data)
    line[3].set_data(x4data, y1data)
      
    if len(y2data) == 1000:
        line[2].set_data(x2data, 2*np.abs(y2data)/(len(y2data)/2))

    return line

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=50 ,
    repeat=False)

plt.show()