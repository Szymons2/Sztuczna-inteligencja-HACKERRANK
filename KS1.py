# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 15:37:51 2022

@author: Admin
"""

def displayPathtoPrincess(n,grid):
#print all the moves here
    start=[]
    pich=[]
    i=0
    while i<m:
        o=0
        print(i)
        while o<m:
            print(o)
            if grid[i][o]=="m": 
                start.append(i)
                start.append(o)
                o=m
                i=m
            o+=1
        i+=1
    i=0
    while i<m:
        o=0
        while o<m:
            if grid[i][o]=="p": 
                pich.append(i)
                pich.append(o)
                o=m
                i=m
            o+=1
        i+=1
    if start[0]<pich[0]:
        while start[0]<pich[0]:
            print("DOWN")
            start[0]+=1
    elif start[0]>pich[0]:
        while start[0]>pich[0]:
            print("UP")
            start[0]-=1

    if start[1]<pich[1]:
        while start[1]<pich[1]:
            print("RIGHT")
            start[1]+=1
    elif start[1]>pich[1]:
        while start[1]>pich[1]:
            print("LEFT")
            start[1]-=1


print("Podaj rozmiar")
m = int(input())
grid = [] 
for i in range(0, m): 
    print("Podaj wiersz")
    grid.append(input().strip())


displayPathtoPrincess(m,grid)