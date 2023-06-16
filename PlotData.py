import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import rfft, rfftfreq
from scipy.signal import find_peaks

def plotGraph(x1Data, y1Data, x2Data, y2Data, showPeak=False):
    
    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[0].legend("Velocity")
    axs[0].set_title("Time Domain")

    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Amplitude')
    axs[1].legend("Velocity from its equilibruim position")
    axs[1].set_title("Frequency Domain")
    
    

    axs[0].plot(x1Data, y1Data)
    axs[1].plot(x2Data, y2Data)

    axs[1].plot([1, 1], [0, 50], color='r')
    axs[1].plot([4, 4], [0, 50], color='r')
    axs[1].plot([25, 25], [0, 50], color='r')
    axs[1].plot([50, 50], [0, 50], color='r')
    axs[1].plot([75, 75], [0, 50], color='r')
    axs[1].plot([100, 100], [0, 50], color='r')

    if showPeak == True:
        # Perform peak detection
        peaks, _ = find_peaks(np.abs(y2Data), height=100)  # Change the height threshold if necessary
        axs[1].plot(x2Data[peaks],y2Data[peaks], 'ro')
        for i in peaks:
            plt.annotate(f"{x2Data[i]:.2f} Hz, {y2Data[i]:.2f} mm/s", (x2Data[i], y2Data[i]), xytext=(3, 3),
            textcoords='offset points', color='black')
        
    fig.tight_layout()
    plt.show()

def compare2Data(x1Data, y1Data, x2Data, y2Data, x3Data, y3Data, x4Data, y4Data):
    
    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Velocity (mm/s)')
    
    axs[0].plot(x1Data, y1Data)
    axs[0].plot(x2Data, y2Data, color = 'r')
    axs[1].plot(x3Data, y3Data)
    axs[1].plot(x4Data, y4Data, color = 'r')
    
    fig.tight_layout()
    plt.show()

def compare3Data(x1Data, y1Data, x2Data, y2Data, x3Data, y3Data, x4Data, y4Data, x5Data, y5Data, x6Data, y6Data):
    
    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[0].set_title("Time Domain")

    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Velocity (mm/s)')
    axs[1].set_title("Frequency Domain")
    axs[1].legend(("500 RPM", "1000 RPM", "1500 RPM"), loc="best")
    
    axs[0].plot(x1Data, y1Data, label = '500 RPM')
    axs[0].plot(x2Data, y2Data, color = 'r', label = '1000 RPM')
    axs[0].plot(x3Data, y3Data, color = 'g', label = '1500 RPM')
    axs[0].legend()
    axs[1].plot(x4Data, y4Data, label = '500 RPM')
    axs[1].plot(x5Data, y5Data, color = 'r', label = '1000 RPM')
    axs[1].plot(x6Data, y6Data, color = 'g', label = '1500 RPM')
    axs[1].legend()
    
    fig.tight_layout()
    plt.show()

def compare4Data(x1Data, y1Data, x2Data, y2Data, x3Data, y3Data, x4Data, y4Data, x5Data, y5Data, x6Data, y6Data):
    
    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[0].set_title("Time Domain")

    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Velocity (mm/s)')
    axs[1].set_title("Frequency Domain")
    
    axs[0].plot(x1Data, y1Data, label = 'no imbalance')
    axs[0].plot(x2Data, y2Data, color = 'r', label = 'imbalance with 1 magnet')
    axs[0].plot(x3Data, y3Data, color = 'g', label = 'imbalance with 2 magnet')
    axs[0].legend()
    axs[1].plot(x4Data, y4Data, label = 'no imbalance')
    axs[1].plot(x5Data, y5Data, color = 'r', label = 'imbalance with 1 magnet')
    axs[1].plot(x6Data, y6Data, color = 'g', label = 'imbalance with 2 magnet')
    axs[1].legend()
    
    fig.tight_layout()
    plt.show()

def compare2Data3d(x1Data, y1Data, x2Data, y2Data):

    # Create the 3D plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the first spectrum
    ax.plot(x1Data, np.zeros_like(x1Data), y1Data, color='red', label='Signal 1')

    # Plot the second spectrum
    ax.plot(x2Data, np.ones_like(x2Data), y2Data, color='blue', label='Signal 2')


    # Set labels and title
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Signal')
    ax.set_zlabel('Magnitude')
    ax.set_title('FFT Spectra Comparison')

    # Set the view angle
    ax.view_init(elev=20, azim=135)

    # Add a legend
    ax.legend()

    # Display the plot
    plt.show()

def plotGraphArduino(x1Data, y1Data, x2Data, y2Data, showPeak=False):
    
    average = sum(y1Data)/len(y1Data)

    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[0].set_title("Time Domain")

    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Amplitude')
    axs[1].set_title("Frequency Domain")
    
    

    axs[0].plot(x1Data, y1Data)
    axs[1].plot(x2Data, y2Data)

    

    if showPeak == True:
        
        # show average of timedomain
        axs[0].plot([0, 2.2], [average, average], color='r', label='Average')
        axs[0].legend()
        axs[0].annotate(f"{average:.2f} mm/s", (2.2, average), xytext=(0, 0), textcoords='offset points', color='black')
        # frequencies of interest
        axs[1].plot([1, 1], [0, 50], color='r', label='Expected frequencies of interest')
        axs[1].annotate(f"Fs", (1, 50), xytext=(-30, 10), textcoords='offset points', color='black', arrowprops=dict(facecolor='black', arrowstyle='->'))
        axs[1].plot([4, 4], [0, 50], color='r')
        axs[1].annotate(f"Fp", (4, 50), xytext=(30, 10), textcoords='offset points', color='black', arrowprops=dict(facecolor='black', arrowstyle='->'))
        axs[1].plot([25, 25], [0, 50], color='r')
        axs[1].annotate(f"Ns", (25, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([50, 50], [0, 50], color='r')
        axs[1].annotate(f"Fl, 2*Ns", (50, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([75, 75], [0, 50], color='r')
        axs[1].annotate(f"3*Ns", (75, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([100, 100], [0, 50], color='r')
        axs[1].annotate(f"2*Fl, 4*Ns", (100, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([125, 125], [0, 50], color='r')
        axs[1].annotate(f"5*Ns", (125, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([150, 150], [0, 50], color='r')
        axs[1].annotate(f"3*Fl, 6*Ns", (150, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([175, 175], [0, 50], color='r')
        axs[1].annotate(f"7*Ns", (175, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([200, 200], [0, 50], color='r')
        axs[1].annotate(f"4*Fl, 8*Ns", (200, 50), xytext=(5, 5), textcoords='offset points', color='black')
        
        # Perform peak detection
        peaks, _ = find_peaks(np.abs(y2Data), height=100)  # Change the height threshold if necessary
        axs[1].plot(x2Data[peaks],y2Data[peaks], 'ro', label='Measured frequency of interest')
        axs[1].legend()
        for i in peaks:
            # plt.annotate(f"{x2Data[i]:.2f} Hz, {y2Data[i]:.2f} mm/s", (x2Data[i], y2Data[i]), xytext=(3, 3),
            # textcoords='offset points', color='black')
            plt.annotate(f"{y2Data[i]:.2f}", (x2Data[i], y2Data[i]), xytext=(5, 5),
            textcoords='offset points', color='black')
        
        # Additional peaks
        xPeak = [26.86, 81.05, 99.61, 131.84, 151.86, 172.36, 200.68]
        yPeak = [29.86, 36.78, 34.78, 39.55, 36.73, 30.53, 20.91]
        axs[1].plot(xPeak, yPeak, 'ro')

        for i, j in zip(xPeak, yPeak):
            plt.annotate(f"{j}", (i, j), xytext=(5, 5),
            textcoords='offset points', color='black')
        
    fig.tight_layout()
    plt.show()

def plotGraphArduino2(x1Data, y1Data, x2Data, y2Data, showPeak=False):
    
    average = sum(y1Data)/len(y1Data)

    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[0].set_title("Time Domain")

    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Amplitude')
    axs[1].set_title("Frequency Domain")
    
    

    axs[0].plot(x1Data, y1Data)
    axs[1].plot(x2Data, y2Data)

    

    if showPeak == True:
        
        # show average of timedomain
        axs[0].plot([0, 2.2], [average, average], color='r', label='Average')
        axs[0].legend()
        axs[0].annotate(f"{average:.2f} mm/s", (2.2, average), xytext=(0, 0), textcoords='offset points', color='black')
        # frequencies of interest
        axs[1].plot([1, 1], [0, 50], color='r', label='Expected frequencies of interest')
        axs[1].annotate(f"Fs", (1, 50), xytext=(-30, 10), textcoords='offset points', color='black', arrowprops=dict(facecolor='black', arrowstyle='->'))
        axs[1].plot([4, 4], [0, 50], color='r')
        axs[1].annotate(f"Fp", (4, 50), xytext=(30, 10), textcoords='offset points', color='black', arrowprops=dict(facecolor='black', arrowstyle='->'))
        axs[1].plot([25, 25], [0, 50], color='r')
        axs[1].annotate(f"Ns", (25, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([50, 50], [0, 50], color='r')
        axs[1].annotate(f"Fl, 2*Ns", (50, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([75, 75], [0, 50], color='r')
        axs[1].annotate(f"3*Ns", (75, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([100, 100], [0, 50], color='r')
        axs[1].annotate(f"2*Fl, 4*Ns", (100, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([125, 125], [0, 50], color='r')
        axs[1].annotate(f"5*Ns", (125, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([150, 150], [0, 50], color='r')
        axs[1].annotate(f"3*Fl, 6*Ns", (150, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([175, 175], [0, 50], color='r')
        axs[1].annotate(f"7*Ns", (175, 50), xytext=(5, 5), textcoords='offset points', color='black')
        axs[1].plot([200, 200], [0, 50], color='r')
        axs[1].annotate(f"4*Fl, 8*Ns", (200, 50), xytext=(5, 5), textcoords='offset points', color='black')
        
        # Perform peak detection
        peaks, _ = find_peaks(np.abs(y2Data), height=100)  # Change the height threshold if necessary
        axs[1].plot(x2Data[peaks],y2Data[peaks], 'ro', label='Measured frequency of interest')
        axs[1].legend()
        for i in peaks:
            # plt.annotate(f"{x2Data[i]:.2f} Hz, {y2Data[i]:.2f} mm/s", (x2Data[i], y2Data[i]), xytext=(3, 3),
            # textcoords='offset points', color='black')
            plt.annotate(f"{y2Data[i]:.2f}", (x2Data[i], y2Data[i]), xytext=(5, 5),
            textcoords='offset points', color='black')
        
        # Additional peaks
        xPeak = [27.34, 79.10, 99.61, 119.63, 147.46, 174.80, 201.17]
        yPeak = [39.87, 32.36, 32.31, 36.27, 53.48, 34.04, 25.78]
        axs[1].plot(xPeak, yPeak, 'ro')

        for i, j in zip(xPeak, yPeak):
            plt.annotate(f"{j}", (i, j), xytext=(5, 5),
            textcoords='offset points', color='black')
        
    fig.tight_layout()
    plt.show()


def plotGraphArduino3(x1Data, y1Data, x2Data, y2Data, showPeak=False):
    
    average = sum(y1Data)/len(y1Data)

    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[0].set_title("Time Domain")

    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Amplitude')
    axs[1].set_title("Frequency Domain")
    
    

    axs[0].plot(x1Data, y1Data)
    axs[1].plot(x2Data, y2Data)

    

    if showPeak == True:
        
        # show average of timedomain
        axs[0].plot([0, 2.2], [average, average], color='r', label='Average')
        axs[0].legend()
        axs[0].annotate(f"{average:.2f} mm/s", (2.2, average), xytext=(0, 0), textcoords='offset points', color='black')
        # frequencies of interest
        # axs[1].plot([1, 1], [0, 50], color='r', label='Expected frequencies of interest')
        # axs[1].annotate(f"Fs", (1, 50), xytext=(-30, 10), textcoords='offset points', color='black', arrowprops=dict(facecolor='black', arrowstyle='->'))
        # axs[1].plot([4, 4], [0, 50], color='r')
        # axs[1].annotate(f"Fp", (4, 50), xytext=(30, 10), textcoords='offset points', color='black', arrowprops=dict(facecolor='black', arrowstyle='->'))
        # axs[1].plot([25, 25], [0, 50], color='r')
        # axs[1].annotate(f"Ns", (25, 50), xytext=(5, 5), textcoords='offset points', color='black')
        # axs[1].plot([50, 50], [0, 50], color='r')
        # axs[1].annotate(f"Fl, 2*Ns", (50, 50), xytext=(5, 5), textcoords='offset points', color='black')
        # axs[1].plot([75, 75], [0, 50], color='r')
        # axs[1].annotate(f"3*Ns", (75, 50), xytext=(5, 5), textcoords='offset points', color='black')
        # axs[1].plot([100, 100], [0, 50], color='r')
        # axs[1].annotate(f"2*Fl, 4*Ns", (100, 50), xytext=(5, 5), textcoords='offset points', color='black')
        # axs[1].plot([125, 125], [0, 50], color='r')
        # axs[1].annotate(f"5*Ns", (125, 50), xytext=(5, 5), textcoords='offset points', color='black')
        # axs[1].plot([150, 150], [0, 50], color='r')
        # axs[1].annotate(f"3*Fl, 6*Ns", (150, 50), xytext=(5, 5), textcoords='offset points', color='black')
        # axs[1].plot([175, 175], [0, 50], color='r')
        # axs[1].annotate(f"7*Ns", (175, 50), xytext=(5, 5), textcoords='offset points', color='black')
        # axs[1].plot([200, 200], [0, 50], color='r')
        # axs[1].annotate(f"4*Fl, 8*Ns", (200, 50), xytext=(5, 5), textcoords='offset points', color='black')
        
        # Perform peak detection
        peaks, _ = find_peaks(np.abs(y2Data), height=40)  # Change the height threshold if necessary
        axs[1].plot(x2Data[peaks],y2Data[peaks], 'ro', label='Measured frequency of interest')
        axs[1].legend()
        for i in peaks:
            # plt.annotate(f"{x2Data[i]:.2f} Hz, {y2Data[i]:.2f} mm/s", (x2Data[i], y2Data[i]), xytext=(3, 3),
            # textcoords='offset points', color='black')
            plt.annotate(f"{y2Data[i]:.2f}", (x2Data[i], y2Data[i]), xytext=(5, 5),
            textcoords='offset points', color='black')
        
        # # Additional peaks
        # xPeak = [27.34, 79.10, 99.61, 119.63, 147.46, 174.80, 201.17]
        # yPeak = [39.87, 32.36, 32.31, 36.27, 53.48, 34.04, 25.78]
        # axs[1].plot(xPeak, yPeak, 'ro')

        # for i, j in zip(xPeak, yPeak):
        #     plt.annotate(f"{j}", (i, j), xytext=(5, 5),
        #     textcoords='offset points', color='black')
        
    fig.tight_layout()
    plt.show()



