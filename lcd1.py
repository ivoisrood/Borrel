#!/usr/bin/python
import os
import smbus
import time
import datetime
import socket

MON_IP = "127.0.0.11"
MON_PORT = 5005

mon = 0

os.chdir("/home/pi/borrel/scripts/log")

I2C_ADDR = 0x27 # I2C device address
LCD_WIDTH = 20   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On 0X08 / Off 0x00

ENABLE = 0b00000100 # Enable bit

E_PULSE = 0.0005
E_DELAY = 0.0005

bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  message = message.ljust(LCD_WIDTH," ")
  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def main():
  lcd_init()

while True:
  f=open('lcd_gps.txt', 'r')
  line=f.readline()
  f.close()
  gps=line.split(",")

  f=open('bme_log.txt', 'r')
  line=f.readline()
  f.close()
  bme=line.split(",")

  f=open('fuel_log.txt', 'r')
  line=f.readline()
  f.close()
  fuel=line.split(",")

  sog=gps[4]
  if float(gps[4]) < 1:
    sog=1
  counter=fuel[0]  
  if float(fuel[0]) < 1:
    counter=1

  lcd_string("SOG " + gps[4] + "km/h   " + gps[1], LCD_LINE_1)
  lcd_string("COG " + gps[5] + "   " + gps[0], LCD_LINE_2)
  #lcd_string(gps[2] + ' - ' + gps[3], LCD_LINE_3)
  lcd_string(str(fuel[0][0:3]) + 'l/h ' + str(round(float(sog)/float(counter), 1)) + 'km/l ' + str(round((float(fuel[1])/1000) ,1)).zfill(4) + 'l', LCD_LINE_3)
  lcd_string("T" + bme[0] + "C RH" +str(bme[2] [0:2]) + "% P" + str(bme[1] [0:4]) + "mb", LCD_LINE_4)
  hack = time.time()
  if hack - mon > 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(str(hack), (MON_IP, MON_PORT))
    mon = hack

  time.sleep(1)
