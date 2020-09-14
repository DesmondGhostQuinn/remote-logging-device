#!/usr/bin/env python3

import socket
import sys
from datetime import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient()
#specify the database and collection being used
db = client.thedb
collection = db.gamer

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
                s1=str(d)   #player tag/code
            if(i==1):
                s2=str(d)   #start time
            if(i==2):
                s3=str(d)   #end time
                
                date_time_obj1 = datetime.strptime(s3, '%x/%X')
                date_time_obj2 = datetime.strptime(s2, '%x/%X')
                duration=date_time_obj1-date_time_obj2
                print(duration)
                ds=duration.seconds
                duration=str(duration)
                my=collection.find_one({'tag':s1})  #finds the player tag/code in the db
                if my:
                    #print("yo")
                    n=my['index']
                    p=my['points']
                n1=str(n)
                n2=n+1
                p2=p+30 #30 points are added for completing the task
                pa=0
                #assign points based on time taken to complete task
                if ds<=180 :
                    pa=pa+60
                elif ds<=500 and dc>180 :
                    pa=pa+50
                elif ds<=600 and ds>500:
                    pa=pa+40
                p3=p2+pa
                if my:
                    #player profile is updated with the new data
                    collection.update(my,{'$set':{'code':s1, 's_time'+n1:s2, 'f_time'+n1:s3, 'duration'+n1:duration, 'index':n2, 'points':p3}})
                else:
                    print("enter an existant code")
            i=i+1
            
            if(i!=1 or i!=0 or i!=2):
                s.close
            if not data:
                print("2")  #for debugging
                break
