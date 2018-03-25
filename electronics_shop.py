#!/bin/python

import sys

def getMoneySpent(keyboards, drives, s):
    max1=-1
    sum1=0
    for elem in keyboards:
        for alum in drives:
            sum1=elem + alum
            if(sum1<=s):
               max1=max(max1,sum1)
    return max1        
        
s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
