import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import revpimodio2
import SensorData as sd
import requests
from pathlib import Path
from time import time

prtg_host = '172.30.230.31'
prtg_host_port = '5050'
prtg_sensor_token = '5678'
interval = 1

currentAverageValue = 0

# create new instance of revpimodio2 in readonly (monitoring) mode
rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)

# catch SIGINT and handle proper release of all IOs
rpi.handlesignalend()
rpi.cycletime = 1000

def average(listData):
    return sum(listData)/len(listData)

def data_gen():
    t1 = time()  
    
    cnt = 0
    while cnt < 10000:
        velocity = sd.read()
        cnt+=1
        t2 = time()
        t_sec = t2-t1
        yield velocity, t_sec

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

ax1.set_ylim(0 , 25)
ax1.set_xlim(0, 100)
ax1.grid()
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Velocity [mm/s]')
ax1.set_title('Time Domain')


ax2.set_ylim(0, 25)
ax2.set_xlim(0, 100)
ax2.grid()
ax2.set_xlabel('Time [s] ')
ax2.set_ylabel('Velocity [mm/s]')
ax2.set_title('Average value')

# initialize the data arrays 
x1data, x2data, y1data, y2data = [], [], [], []
peakAverage = []
downAverage = []
tresholdWarning = 2
tresholdInterrupt = 1
flag = False
def run(data):
    global flag
    global currentAverageValue
    # update the data
    y1, t_sec = data
    
    
    if y1 > tresholdWarning:
        
        peakAverage.append(y1)
        downAverage.clear()
        y2data.append(average(peakAverage))
        currentAverageValue = average(peakAverage)

    else:
        downAverage.append(y1)
        peakAverage.clear()
        y2data.append(average(downAverage))
        currentAverageValue = average(downAverage)
    
    x1data.append(t_sec)
    y1data.append(y1)
    
    
    x2data.append(t_sec)
    # axis limits checking. Same as before, just for both axes
    
    xmin, xmax = ax1.get_xlim()
    if t_sec >= xmax:
        ax1.set_xlim(xmin, 2*xmax)
        ax1.figure.canvas.draw()
        ax2.set_xlim(xmin, 2*xmax)
        ax2.figure.canvas.draw()
    
    

    # update the data of both line objects
    line[0].set_data(x1data, y1data)
    line[1].set_data(x2data, y2data)
      
    # Sent to PRTG
    json_response = {
        "prtg": {
            "result": [
                {
                    "channel": "vibration",
                    "value": int(y1 * 100)
                },
                {
                    "channel": "peak value",
                    "value": int(currentAverageValue * 100)
                }
            ]
        }
    }
    # print output for debugging
    print(json_response)
    json_string = str(json_response)
    json_string = str.replace(json_string, '\'', '\"')
    prtg_request_URL = 'http://' + prtg_host + ':' + prtg_host_port + '/' + prtg_sensor_token + '?content=' + json_string
    print(prtg_request_URL)
    request = requests.get(prtg_request_URL)
    print(request.status_code)
    
    return line


ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=200 ,
    repeat=False)
fig.tight_layout()
plt.show()
