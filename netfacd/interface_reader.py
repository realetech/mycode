#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

print("starting for loop")

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
        print('IP: ', end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
    except:
        print('Could not collect adapter information')
