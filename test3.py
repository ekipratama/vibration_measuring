from scipy.fftpack import rfft, rfftfreq

temp = [1900, 1920, 2000]

print(rfft(temp))
print(rfftfreq(len(temp), 1/2000))