#!/usr/bin/python
import serial
import math
import socket

gps=serial.Serial('/dev/ttyUSB_GPS', 4800, timeout=1)

GPS_IP="127.0.0.2"
GPS_PORT=5005

avgnr=10    # average numbers

soglist=[0]*avgnr   # setup arrays for SOG and COG

xlist=[0]*avgnr

ylist=[0]*avgnr

i=0

def time():
    hh=int(data[1][0:2])+2
    if hh >= 24:
        hh=hh-24
    else:
        hh=hh
    mm=data[1][2:4]
    return hh+ ':' + mm

def date():
    dd=data[9][0:2]
    mon=data[9][2:4]
    year=data[9][4:6]
    return dd + '-' + mon + '-' + year

def lat():
    ddla=data[3][0:2]
    mmla=str(round(float(data[3][2:8]), 1))
    return ddla + '-' + mmla + data[4]

def long():
    ddlo=data[5][0:3]
    mmlo=str(round(float(data[5][3:8]), 1))
    return ddlo + '-' + mmlo + data[6]

while True:
    gps_raw=gps.readline() # read from GPS
    data=gps_raw.split()
    if str(data[0] [3:6]) == 'RMC': # check for NMEA sentence with RMC-data
        RMC=str(data [0])
        data=RMC.split(",")
        if data[2] == "A": # check for valid sentence
            sog=round(float(data[7]), 1)
            cog=math.radians(round(float(data[8]), 1))
            soglist[i]=sog              # put SOG in array
            xlist[i]=math.cos(cog)      # put sin/cos of COG in array
            ylist[i]=math.sin(cog)
            i+=1                       # advance to next position in array
            if i == avgnr:
                i=0
            sog=str(sum(soglist)/len(soglist)*1.852).zfill(4)   # sum array and divide by length of array to calulcate average
            cog=str(round(math.degrees(math.atan2(sum(ylist), sum(xlist))), 1)).zfill(5)
            if cog < 0:
                cog=cog+360
            f=open('/home/pi/borrel/scripts/log/lcd_gps.txt', 'w')
            f.write(date() + ',' + time() + ',' + lat() + ',' + long() + ',' + sog + ',' + cog)
            f.close()
            print(date() + ',' + time() + ',' + lat() + ',' + long() + ',' + sog + ',' + cog)

        sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # send data to NMEA-multiplexer
        sock.sendto(gps_raw,(GPS_IP, GPS_PORT))


    
