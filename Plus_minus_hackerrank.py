#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    arr_length=len(arr)
    a=0
    b=0
    c=0
    for i in arr:
        if(i>0):
            a=a+1
        elif(i<0):
            b=b+1
        else:
            c=c+1
    positive=a/arr_length
    negative=b/arr_length
    zero=c/arr_length
    print(positive)
    print(negative)
    print(zero)
   
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
