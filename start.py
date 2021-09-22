#!/usr/bin/env python
import serial
import operator
import time
import os
import sys

os.chdir("/home/pi/borrel/scripts")

#start GPS
os.system("./gps.py &")
print("GPS start")

#start GPS_log
os.system("./gps_log.py &")
print("log read open")

#start temp sensors
os.system("./temp.py &")
print("Temp sensors on")

#start BME
os.system("./bme.py &")
print("BME-280 on")

#start Fuel counter
os.system("./fuel.py &")
print("Fuel counter on")

#start IMU
os.system("./imu.py &")
print("IMU-9250 on")

#start BMV
os.system("./bmv.py &")
print("BMV on")

#start MPPT
os.system("./mppt.py &")
print("MPPT on")

#start K-Plex
os.system("sudo kplex -f /home/pi/borrel/kplex/kplex.conf &")
print("K-Plex start")

#start LCD's
os.chdir("/home/pi/borrel/scripts/lcd")
os.system("./lcd1.py &")
os.system("./lcd2.py &")
os.system("./lcd_check.py &")
print("LCD 1&2 on")

#start AIS
os.chdir("/home/pi/borrel/rtl-ais")
os.system("./rtl_ais -g 35 -h 127.0.0.3 -P 5005 &")
print("ais start")
