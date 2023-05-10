import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import revpimodio2
import time
from scipy.fftpack import rfft, rfftfreq
import numpy as np

# Parameters
x_len = 200
y_range = [1500, 2500]

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
xs = list(range(0, 200))
ys = [0] * x_len
ax.set_ylim(y_range)


line, = ax.plot(xs, ys) 

# Format plot
# ax.xlabel('Samples')
# ax.title('Vibration over Time')
# ax.ylabel('RMS')


# This function is called periodically from FuncAnimation
def animate(i, ys):

    # Read temperature (Celsius) from TMP102
    sensor_data = rpi.io.AIn_2.value

    # Add y to list
    ys.append(sensor_data)
    
    # Limit y list to set number of items
    ys = ys[-x_len:]
    yf = rfft(ys)
    xf = rfftfreq(len(yf), 1/len(yf))
    # Update line with new Y values
    line.set_ydata(ys)
    
    ax2.plot(xf, np.abs(yf))
    return line,

# create new instance of revpimodio2 in readonly (monitoring) mode
rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)

# catch SIGINT and handle proper release of all IOs
rpi.handlesignalend()    

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval=50, blit=True)
plt.show()
