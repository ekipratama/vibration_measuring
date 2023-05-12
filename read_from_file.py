import revpimodio2
from pathlib import Path

file = open('/sys/bus/iio/devices/iio:device1/in_voltage1_raw', 'r')

def loop (cycletools):
    sensorData = Path('/sys/bus/iio/devices/iio:device1/in_voltage1_raw').read_text()
    volt = ((int (sensorData) * 12500) >> 21) + 6250
    print(volt)

# create new instance of revpimodio2 in readonly (monitoring) mode
rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)

# catch SIGINT and handle proper release of all IOs
rpi.handlesignalend()

# start cycle loop, cycle time in milliseconds
rpi.cycleloop(loop, cycletime=250)