import numpy as np
import matplotlib.pyplot as plt
import readWriteData as rwd

# Simulated time-domain signal


# readedData = rwd.loadNpy("samples/vibration_50hz_left_bearing_cycletime_250_normal.npy")


# xTime = readedData[0]
# yTime = readedData[1]

xTime = []
yTime = []
with open('samples/samples_300rpm_unbalance_2_sensor_ifm_sp_10k_bearing.txt', 'r') as file:
    for line in file:
        # Extract x and y values from each line
        x, y = line.strip().split(',')
        x = float(x)
        y = float(y)

        # Append the values to the samples list
        xTime.append(x)
        yTime.append(y)

time_signal = yTime


# Rotation speed in Hz
rotation_speed_RPM = 1500

# Resampling based on rotation speed
time_interval = 60 / rotation_speed_RPM
resampled_signal = np.interp(np.arange(0, len(time_signal), time_interval), np.arange(len(time_signal)), time_signal)

# Compute Fourier Transform
frequency_signal = np.fft.fft(resampled_signal)
frequency_signal[0] = 0

# Extract orders of interest (e.g., first three harmonics)
order_1 = frequency_signal[int(rotation_speed_RPM/60)]
order_2 = frequency_signal[int(2 * rotation_speed_RPM/60)]
order_3 = frequency_signal[int(3 * rotation_speed_RPM/60)]
# Plot order spectrum
frequency_bins = np.fft.fftfreq(len(frequency_signal)) * rotation_speed_RPM
plt.plot(frequency_bins, np.abs(frequency_signal))
plt.xlabel('Frequency (RPM)')
plt.ylabel('Amplitude')
plt.title('Order Spectrum')
plt.grid(True)
plt.show()
print(order_1)
print(order_2)
print(order_3)
