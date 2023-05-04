#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:et

import revpimodio2
import time

def loop(cycletools):
    timestamp_milliseconds = int(round(time.time() * 1000))
    
    analog_value1 = rpi.io.AIn_1.value
    analog_value2 = rpi.io.AIn_1.value
    
    print(timestamp_milliseconds, analog_value1, analog_value2)
    
# create new instance of revpimodio2 in readonly (monitoring) mode
rpi = revpimodio2.RevPiModIO(autorefresh=True, monitoring=True)

# catch SIGINT and handle proper release of all IOs
rpi.handlesignalend()

# start cycle loop, cycle time in milliseconds
rpi.cycleloop(loop, cycletime=20)