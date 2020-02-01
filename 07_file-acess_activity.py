# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:28:33 2020

@author: CEC
"""

file = open("devices.txt","a")
newItem=""
while True:
    newItem = input("Enter new Item:")
    if newItem == "exit":
        print("All donde!")
        break
    file.write(newItem+"\n")
file.close()