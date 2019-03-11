#!/usr/bin/env python3

import socket
import sys
from datetime import datetime


HOST = "127.0.0.1"  # The server's hostname or IP address
#HOST="192.168.0.101"
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #str=''
    """"arga = sys.argv[1]
    argb = sys.argv[2]
    argc = sys.argv[3]
    argd = sys.argv[4]
    str=arga+argb+argc+argd"""
    str=input("enter the code")
    s.send(str.encode())
    t=datetime.now()
    str2=t.strftime('%x/%X')
    s.send(str2.encode())
    print("data sent")
    stro=input("enter the option")
    t2=datetime.now()
    str3=t2.strftime('%x/%X')
    s.send(str3.encode())
    """""duration=t2-t
    duration=duration.strftime('%x/%X')
    s.send(duration.encode())"""
    #s.sendall(message.encode("hello world"))
    data = s.recv(1024)


print("Received", repr(data))
