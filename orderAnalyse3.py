import numpy as np
import scipy as sc

rpm = 300
xTime = []
yTime = []
with open('samples/samples_300rpm_unbalance_sensor_ifm_sp_10k_bearing.txt', 'r') as file:
    for line in file:
        # Extract x and y values from each line
        x, y = line.strip().split(',')
        x = float(x)
        y = float(y)

        # Append the values to the samples list
        xTime.append(x)
        yTime.append(y)


# round per sample
sample_rate = len(yTime)/max(xTime)
round_per_sample = (rpm / 60) / sample_rate


# itegrate the speed signal to obtain shaft rounds position
shaft_rounds_position = np.cumsum(round_per_sample)

# resample data
x = shaft_rounds_position
y = yTime
f = sc.interpolate.interp1d(x, y)
xnew = np.linspace(min(shaft_rounds_position), max(shaft_rounds_position), num=len(shaft_rounds_position))
ynew = f(xnew)

# new sampele rate out of value-distance of new x-axis
new_periodtime = xnew[2] - xnew[1]
new_sample_rate = 1/new_periodtime

# fft
fft_freq, fft_amplitude = filter_window_fft(ynew, new_sample_rate)