#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    i1=0
    j1=0
    i2=0
    j2=len(arr)-1
    for k in range(len(arr)):    
        sum1 += arr[i1][j1]
        #print(arr[i1][j1])
        i1 += 1
        j1 += 1
        sum2 += arr[i2][j2]
        #print(arr[i2][j2])
        i2 += 1
        j2 -= 1
    diff = abs(sum1-sum2)
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
