#!/usr/bin/python
import os
import time
import socket
import select

#LCD1
LCD1_IP = "127.0.0.11"
LCD1_PORT = 5005
lcd1sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lcd1sock.bind((LCD1_IP, LCD1_PORT))

#LCD2
LCD2_IP = "127.0.0.12"
LCD2_PORT = 5005
lcd2sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lcd2sock.bind((LCD2_IP, LCD2_PORT))

lcd1_hack = time.time()
lcd2_hack = time.time()

os.chdir("/home/pi/borrel/scripts/lcd/")

while True:
    #LCD 1
    lcd1ready = select.select([lcd1sock], [], [], .1)
    if lcd1ready [0]:
        data, addr = lcd1sock.recvfrom(1024)
        lcd1_hack = float(data)
    if time.time() - lcd1_hack > 10:
        os.system("./lcd1kill.py &")
        time.sleep(2)
        os.system("./lcd1.py &")
        lcd1_hack = time.time()

    #LCD 2
    lcd2ready = select.select([lcd2sock], [], [], .1)
    if lcd2ready [0]:
        data, addr = lcd2sock.recvfrom(1024)
        lcd2_hack = float(data)
    if time.time() - lcd2_hack > 10:
        os.system("./lcd2kill.py &")
        time.sleep(2)
        os.system("./lcd2.py &")
        lcd2_hack = time.time()

    time.sleep(1)
