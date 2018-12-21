#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    countPos = 0
    countNeg = 0
    countZero = 0
    for i in arr:
        if i>0:
            countPos += 1
        elif i==0:
            countZero += 1
        else:
            countNeg += 1
    print(countPos/len(arr))
    print(countNeg/len(arr))
    print(countZero/len(arr))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
