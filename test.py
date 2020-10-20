# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:39:10 2020

@author: mecha
"""

import serial
import time
import io
arduinodata=serial.Serial('com4',baudrate=9600,timeout=1)
time.sleep(2)
sio = io.TextIOWrapper(io.BufferedRWPair(arduinodata, arduinodata))
while 1:
    # sio.flush()
    # tempo=int(100)
    # # output=str(tempo)
    # # tempo='100'
    # output=str(tempo)
    # arduinodata.flush()
    # print("Python value sent:")
    # print(output)
    # arduinodata.write("Hello")
    # # sio.write(output)
    time.sleep(1)
    arduinodata.reset_output_buffer()
    arduinodata.reset_input_buffer()
    temp=int(100)
    arduinodata.write(b'p')
    print(temp)
    time.sleep(10)
    # if arduinodata.in_waiting > 0:
    
    # i=0
    # for i in range(3):
    #     x=arduinodata.read()
    #     data.append(x)
        
    #     i=i+1
    # print("Arduino data")
    # print(str(data))
     # time.sleep(5)
   
   
    
    
    
    # msg=arduinodata.readline()
    # print("Message Arduino got:")
    # print(msg)
    
    
    # print("Message after decoding:")
    # msgd=msg.decode()
    # print(msgd)
    
    # time.sleep(3) 
    # arduinodata.flush()
    

