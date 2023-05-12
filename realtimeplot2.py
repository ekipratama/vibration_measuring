import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
xdata2,ydata2= [], []
ln, = plt.plot([], [], 'ro') 
ln2, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,ln2

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)

    xdata2.append(frame)
    ydata2.append(np.cos(frame))
    ln2.set_data(xdata2,ydata2)
    
    return ln,ln2

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)


plt.show()