# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:54:21 2023

@author: louis
"""

import sys


tests = int(sys.stdin.readline())
res = []

for _ in range(tests):
    highest = 0
    highest_index = -1
    n = int(sys.stdin.readline())
    frogs = sys.stdin.readline().rstrip().split(" ")
    hash_map = {i:0 for i in range(1,n+1)}
    for i,frog in enumerate(frogs):
        k = int(frog)
        while k <= n:
            hash_map[k] +=1
            if hash_map[k] > highest:
                highest = hash_map[k]
                highest_index = k
                
            k += int(frog)
    res.append(highest_index)
for i in res:
    print(i,file=sys.stdout)
                
            
    