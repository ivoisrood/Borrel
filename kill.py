#!/usr/bin/env python
import os
import time

os.chdir("/home/pi/borrel/scripts")

# stop Monitor
os.system("pkill -f ./start.py &")
print("monitor stop")

# stop Kplex
os.system("sudo pkill kplex &")
print("K-Plex stop")

#stop GPS
os.system("pkill -f ./gps.py &")
print("GPS stop")

#stop GPS_log
os.system("pkill -f ./gps_log.py &")
print("log read stop")

#stop Fuel counter
os.system("pkill -f ./fuel.py &")
print("Fuel counter stop")

#stop IMU
os.system("pkill -f ./imu.py &")
print("IMU-9250 stop")

#stop temp sensors
os.system("pkill -f ./temp.py &")
print("Temp sensors stop")

#stop BME
os.system("pkill -f ./bme.py &")
print("BME-280 stop")

#stop BMV
os.system("pkill -f ./bmv.py &")
print("BMV stop")

#stop MPPT
os.system("pkill -f ./mppt.py &")
print("MPPT stop")

#stop LCD's
os.chdir("/home/pi/borrel/scripts/lcd")
os.system("./lcd1kill.py &")
os.system("./lcd2kill.py &")
os.system("pkill -f ./lcd_check.py &")
print("LCD 1&2 off")

#stop AIS
os.chdir("/home/pi/borrel/rtl-ais")
os.system("pkill -f ./rtl_ais &")
print("ais stop")


