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
    while cnt < 10000:
        sensorData = Path('/sys/bus/iio/devices/iio:device1/in_voltage1_raw').read_text()
        volt = ((int (sensorData) * 12500) >> 21) + 6250
#         volt = rpi.io.AIn_2.value
        velocity = ((volt - 1880)/8120) * 25
        cnt+=1
        t += 1
        y1 = velocity
        t2 = time()
        t_sec = t2-t1
        yield t, y1, t_sec

data_gen.t = 0

# create a figure with four subplots
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.set_figwidth(14)
fig.set_figheight(9)
fig.tight_layout()
# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')

line = [line1, line2]

# the same axes initalizations as before (just now we do it for both of them)

ax1.set_ylim(0 , 10)
ax1.set_xlim(0, 100)
ax1.grid()
ax1.set_xlabel('Samples')
ax1.set_ylabel('Velocity [mm/s]')


ax2.set_ylim(0, 10 )
ax2.set_xlim(0, 100)
ax2.grid()
ax2.set_xlabel('Time [s] ')
ax2.set_ylabel('Velocity [mm/s]')


# initialize the data arrays 
x1data, x2data, y1data, y2data = [], [], [], []

def run(data):
    # update the data
    t, y1, t_sec = data
    x1data.append(t)
    y1data.append(y1)
    
    y2data = y1data
    
    x2data.append(t_sec)
    # axis limits checking. Same as before, just for both axes
    
    xmin, xmax = ax1.get_xlim()
    if t >= xmax:
        ax1.set_xlim(xmin, 2*xmax)
        ax1.figure.canvas.draw()
        ax2.set_xlim(xmin, 2*xmax)
        ax2.figure.canvas.draw()
    
#     ymin, ymax = ax1.get_ylim()
#     ymin = min(y1data)
#     if y1 >= ymax:
#         ax1.set_ylim(ymin, 1.002*ymax)
#         ax1.figure.canvas.draw()
#         ax2.set_ylim(ymin, 1.002*ymax)
#         ax2.figure.canvas.draw()
    
    
    

    # update the data of both line objects
    line[0].set_data(x1data, y1data)
    line[1].set_data(x2data, y1data)
      

    return line

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=200 ,
    repeat=False)

plt.show()