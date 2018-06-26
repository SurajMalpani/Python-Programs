# -*- coding: utf-8 -*-
"""
Created on Thu May 24 19:25:51 2018

@author: suraj
"""

#*hailstone number : number of iterations it takes to reach 1
import time

start=time.process_time()
hailstone = [0]
for st in range(1,100):
    x = st
    count = 0
    while x !=1:
        if x < st:
            count += hailstone[x]    #Dynamic programming
            break
        if x%2==0:
            x//=2
        else:
            x=(3*x+1)
        count+=1
    #print(st,count)
    hailstone.append(count)
print(max(hailstone))
#print(hailstone[10])
print(time.process_time()-start)   #time it takes to perform above oprn
    
def hailstone(x):
    while x !=1:
        if x%2==0:
            x//=2
        else:
            x=(3*x+1)
        return x

hailstone(7)
