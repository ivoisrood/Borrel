#!/usr/bin/env python
import os
import time

#stop LCD's
os.chdir("/home/pi/borrel/scripts/lcd")
os.system("./lcd1kill.py &")
os.system("./lcd2kill.py &")
print("LCD 1&2 off")

time.sleep(2)

#start LCD's
os.system("./lcd1.py &")
os.system("./lcd2.py &")
print("LCD 1&2 on")
