# !/usr/bin/env python


import socket
import time
import random

#variables
count = 0
rand1 = 0
rand2 = 0
count1 = 0
sensorid = 201
sensorid2 = 1

TCP_IP = '127.0.0.1'

TCP_PORT = 5007

BUFFER_SIZE = 500


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#conn, addr = s.accept()
while(1):
#sensors 1-5 are Oxygen sensors
#sensors 6-10 are Smoke/Gas detection sensors
#sensors 11-15 are Luminosity sensors
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
      if(sensorid==301):
            sensorid=201
s.close()
