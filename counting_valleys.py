#!/bin/python

import sys

def countingValleys(n, s):    
    for i in range(n):
        if(s[i]=='U'):
            counter+=1
        elif(s[i]=='D'):
            counter-=1
        if(counter==0 and (s[i]=='U')):
            valcount+=1
    return valcount

    
            
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    s = raw_input().strip()
    result = countingValleys(n, s)
    print result
