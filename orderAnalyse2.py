import numpy as np
import matplotlib.pyplot as plt

# Simulated time-domain signal
# xTime = []
# yTime = []
# with open('samples/samples_300rpm_unbalance_sensor_ifm_sp_10k_bearing.txt', 'r') as file:
#     for line in file:
#         # Extract x and y values from each line
#         x, y = line.strip().split(',')
#         x = float(x)
#         y = float(y)

#         # Append the values to the samples list
#         xTime.append(x)
#         yTime.append(y)

data_list = []
sample_rate = 2000
data_point = 4096
duration = data_point/sample_rate
with open('samples/arduino_1500rpm_unbalance_4096s.txt', 'r') as file:
    for line in file:
        data_list.append(float(line))

xTime = np.arange(0, 2.048, 0.0005) # 2000 hz
yTime = data_list

time_signal = yTime

# Rotation speed in Hz
rotation_speed = 25

# Resampling based on rotation speed
time_interval = 1 / rotation_speed
resampled_signal = np.interp(np.arange(0, len(time_signal), time_interval), np.arange(len(time_signal)), time_signal)

# Compute Fourier Transform
frequency_signal = np.fft.fft(resampled_signal)

# Extract orders of interest (e.g., first three harmonics)
order_1 = frequency_signal[rotation_speed]
order_2 = frequency_signal[2 * rotation_speed]
order_3 = frequency_signal[3 * rotation_speed]

# Plot order spectrum
frequency_bins = np.fft.fftfreq(len(frequency_signal)) * rotation_speed
plt.plot(frequency_bins, np.abs(frequency_signal))
plt.xlabel('Order')
plt.ylabel('Amplitude')
plt.title('Order Spectrum')
plt.grid(True)
plt.show()

