# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:49:14 2020

@author: utob
"""

command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print ("car is already started!")
        else:
            started = True 
            print("car started...")
    elif command == "stop":
        if not started:
            print("car  is already stoped")
        else:
            started = False
            print("car stopped.")
    elif command == "help":
        # vaghty ke az triple cotation estefade mikoni 
        #havaset bashe neveshteha ro bekeshi aval khat#
        print("""
star - to star the car
stop - to stop the car
quit - to quit the car
              """)
    elif command == "quit":
        break
    else:
        print("sorry, i dont understand the command ")