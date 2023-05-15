import numpy as np
from scipy.fftpack import fft, rfft
from scipy.fftpack import fftfreq, rfftfreq
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from Signal_Generator_class import Signal

# Generate the three signals using Signal class and its method sine()
signal_1hz = Signal(amplitude=3, frequency=1, sampling_rate=200, duration=2)
sine_1hz = signal_1hz.sine()
signal_20hz = Signal(amplitude=1, frequency=20, sampling_rate=200, duration=2)
sine_20hz = signal_20hz.sine()
signal_10hz = Signal(amplitude=0.5, frequency=10, sampling_rate=200, duration=2)
sine_10hz = signal_10hz.sine()

# Sum the three signals to output the signal we want to analyze
signal = sine_1hz + sine_20hz + sine_10hz

# Plot the signal
# plt.plot(signal_1hz.time_axis, signal, 'b')
# plt.xlabel('Time [sec]')
# plt.ylabel('Amplitude')
# plt.title('Sum of three signals')
# plt.show()

# Apply the FFT on the signal
fourier = rfft(signal)

# Calculate N/2 to normalize the FFT output
N = len(signal)
normalize = N/2

# Get the frequency components of the spectrum
sampling_rate = 200.0
frequency_axis = rfftfreq(N, d=1.0/2000)
norm_amplitude= (2*np.abs(fourier))/N

print(N)

# Plot the result (the spectrum |Xk|)
# plt.plot(frequency_axis, norm_amplitude)
# plt.xlabel('Frequency[Hz]')
# plt.ylabel('Amplitude')
# plt.title('Spectrum')
# plt.show()
