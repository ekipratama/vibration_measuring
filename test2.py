import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import rfft, rfftfreq

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

x, y = generate_sine_wave(200, 4000, 5)

sample_rate = 4000
duration = 5

n = sample_rate * duration

yf = rfft(y)
xf = rfftfreq(n, 1/sample_rate)

plt.plot(xf, np.abs(yf))
plt.show()
