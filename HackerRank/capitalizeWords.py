#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = s.split(" ")
    b = []
    for i in l:
        a = i.capitalize()
        b.append(i.capitalize() for i in l)
    # l = list(s)
    # l[0] = l[0].upper()
    # i = 1
    # while(i<len(l)):
    #     if(l[i]==' ' and i<len(l)):
    #         l[i+1] = l[i+1].upper()
    #         i += 1
    #     i += 1
    # s = ''.join(l)
    return ' '.join(b)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
