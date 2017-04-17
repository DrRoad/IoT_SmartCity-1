# !/usr/bin/env python


import socket
import time
import random

#variables
count = 0
rand1 = 0
rand2 = 0
count1 = 0
sensorid = 701
sensorid2 = 1

TCP_IP = '127.0.0.8'

TCP_PORT = 5005

BUFFER_SIZE = 500


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#conn, addr = s.accept()
while(1):
#sensors 1-200 are Oxygen sensors
#sensors 200- 400are Smoke/Gas detection sensors
#sensors 400-600 are Parking sensors
#sensors 600- 800 are Luminosity sensors
#sensors 800-1000 are Garbage sensors
      rand1 = (random.randint(8,21))
      t = str(sensorid).encode()
      print sensorid
      s.send(t)
      s.send(",")
      m = str(rand1).encode()
      s.send(m)
      s.send("\n")
      sensorid = sensorid+1
      time.sleep(1)
      if(sensorid==801):
            sensorid=701
s.close()
