#!/usr/bin/env python3

import socket

import sys
from datetime import datetime

import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.thedb
collection = db.gamerz

#HOST = "192.168.0.101"
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

toi=""
i=0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            d=data.decode('utf-8')
            print(d)
            if(i==0):
                s1=str(d)
            if(i==1):
                s2=str(d)
            if(i==2):
                s3=str(d)
                date_time_obj1 = datetime.strptime(s3, '%x/%X')
                date_time_obj2 = datetime.strptime(s2, '%x/%X')
                duration=date_time_obj1-date_time_obj2
                print(duration)
                duration=str(duration)
                my=collection.find_one({'code':s1})
                if my:
                    print("yo")
                    n=my['index']
                #n=my['index']
                #n=2
                #print(n)
                n1=str(n)
                n2=n+1
                #my=mongo.db.gamerz.find_one({'code':s1}) #added recently for checking before creating doc
                if my:
                    collection.update(my,{'$set':{'code':s1, 's_time'+n1:s2, 'f_time'+n1:s3, 'duration'+n1:duration, 'index':n2}})
                else:
                    print("enter an existant code")
            i=i+1
            if(i!=1 or i!=0 or i!=2):
                s.close
            if not data:
                print("2")  #for debugging
                break
