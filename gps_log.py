#!/usr/bin/python
import time as t
import os
import math

os.chdir("/home/pi/borrel/scripts/log")

x2=x3=x4=x5=x6=x7=x8=x9=x10=0

y2=y3=y4=y5=y6=y7=y8=y9=y10=0

sog2=sog3=sog4=sog5=sog6=sog7=sog8=sog9=sog10=0

count=0

def time():
    hh=str(int(data[1][0:2])+2)
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
    f=open('gps_log.txt', 'r')
    line=f.readline()
    f.close()
    data=line.split(',')
    if data[0][3:6] == 'RMC':
        count=count+1
        sog=round(float(data[7]), 1)
        cog=math.radians(round(float(data[8]), 1))
        if count == 1:
            x1=math.cos(cog)
            y1=math.sin(cog)
            sog1=sog
        if count == 2:
            x2=math.cos(cog)
            y2=math.sin(cog)
            sog2=sog
        if count == 3:
            x3=math.cos(cog)
            y3=math.sin(cog)
            sog3=sog
        if count == 4:
            x4=math.cos(cog)
            y4=math.sin(cog)
            sog4=sog
        if count == 5:
            x5=math.cos(cog)
            y5=math.sin(cog)
            sog5=sog
        if count == 6:
            x6=math.cos(cog)
            y6=math.sin(cog)
            sog6=sog
        if count == 7:
            x7=math.cos(cog)
            y7=math.sin(cog)
            sog7=sog
        if count == 8:
            x8=math.cos(cog)
            y8=math.sin(cog)
            sog8=sog
        if count == 9:
            x9=math.cos(cog)
            y9=math.sin(cog)
            sog9=sog
        if count == 10:
            x10=math.cos(cog)
            y10=math.sin(cog)
            sog10=sog
            count=0
        xtot=x1+x2+x3+x4+x5+x6+x7+x8+x9+x10
        ytot=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10
        cog=round(math.degrees(math.atan2(ytot, xtot)), 1)
        if cog < 0:
            cog=cog+360
        cog=str(cog).zfill(5)
        sog=str(round((((sog1+sog2+sog3+sog4+sog5+sog6+sog7+sog8+sog9+sog10)/10)*1.852), 1)).zfill(4)
        f=open('lcd_gps.txt', 'w')
        f.write(date() + ',' + time() + ',' + lat() + ',' + long() + ',' + sog + ',' + cog)
        f.close()
        print(date() + ',' + time() + ',' + lat() + ',' + long() + ',' + sog + ',' + cog)
        t.sleep(1)
    else:
        t.sleep(1)

    
