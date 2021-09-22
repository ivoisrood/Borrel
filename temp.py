#!/usr/bin/python
import serial
import os

temp=serial.Serial('/dev/ttyUSB_TEMP', 9600, timeout=1)
temp.flush()

while True:
    if temp.in_waiting > 0:
        line=temp.readline().decode('utf-8').rstrip()
        #print(str(line))
        line=line.split(',')
        temp1=line[1][0:4]
        temp2=line[3][0:4]
        temp3=line[5][0:4]
        temp4=line[7][0:4]
        os.chdir("/home/pi/borrel/scripts/log")
        f=open('temp_log.txt', 'w')
        f.write((str(temp1).zfill(4))+","+(str(temp2).zfill(4))+","+(str(temp3).zfill(4))+","+(str(temp4).zfill(4)))
        f.close()
        print((str(temp1).zfill(4))+","+(str(temp2).zfill(4))+","+(str(temp3).zfill(4))+","+(str(temp4).zfill(4)))
        

    
