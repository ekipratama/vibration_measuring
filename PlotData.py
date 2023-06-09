import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import rfft, rfftfreq

def plotGraph(x1Data, y1Data, x2Data, y2Data):
    
    fig, axs = plt.subplots(2)
    
    axs[0].grid()
    axs[0].set_xlabel('Time (sec)')
    axs[0].set_ylabel('Velocity (mm/s)')
    axs[0].legend("Velocity")
    axs[0].set_title("Time Domain")

    axs[1].grid()
    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Velocity (mm/s)')
    axs[1].legend("Velocity from its equilibruim position")
    axs[1].set_title("Frequency Domain")
    
    axs[0].plot(x1Data, y1Data)
    axs[1].plot(x2Data, y2Data)
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


