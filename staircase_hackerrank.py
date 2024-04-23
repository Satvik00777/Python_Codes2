import math
import os
import random
import re
import sys



def staircase(n):
    a=1
    for i in range(n):
        print(" "*(n-a)+("#"*a))
        a+=1
        
    
   
    
          
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)