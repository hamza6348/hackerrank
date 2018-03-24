#!/bin/python

import sys

def sockMerchant(n, ar):
    count={}
    sum1=0
    for t in ar:
        if t in count.keys():
            count[t] += 1
        else:
            count[t] = 1
    for t in count.values():
        if(t>1):
            sum1=sum1+t/2
    return sum1        
        

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
