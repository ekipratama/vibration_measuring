#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:et

import revpimodio2
import time
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import rfft, rfftfreq

analog_value2 = []

def loop(cycletools):
    timestamp_milliseconds = int(round(time.time() * 1000))
    
    if len(analog_value2) < 1000:
        analog_value2.append(rpi.io.AIn_2.value)
    elif len(analog_value2) == 1000:
             
             yf = rfft(analog_value2)
             xf = rfftfreq(len(analog_value2), 1/2000)
             plt.ylim([0, 5000])
             plt.plot(xf, np.abs(yf))
             plt.show()
    
    print(len(analog_value2))
    
# create new instance of revpimodio2 in readonly (monitoring) mode
rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)

# catch SIGINT and handle proper release of all IOs
rpi.handlesignalend()

# start cycle loop, cycle time in milliseconds
rpi.cycleloop(loop, cycletime=20)