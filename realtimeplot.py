import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


# Parameters
x_len = 200
y_range = [0, 10]

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200))
ys = [0] * x_len
ax.set_ylim(y_range)

line, = ax.plot(xs, ys) 

# Format plot
plt.xlabel('Samples')
plt.title('Vibration over Time')
plt.ylabel('RMS')


# This function is called periodically from FuncAnimation
def animate(i, ys):

    # Read temperature (Celsius) from TMP102
    sensor_data = random.randint(0, 10)

    # Add y to list
    ys.append(sensor_data)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)
    
    return line,

    

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval=50, blit=True)
plt.show()
