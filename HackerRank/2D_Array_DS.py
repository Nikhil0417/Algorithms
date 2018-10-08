#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    s = []
    # for k in range(0,4):
    #     for j in range(0,4):
    #         sum = 0
    #         for i in range(0+j,3+j):
    #             sum = sum + arr[i][k] + arr[i][k+1] + arr[i][k+2]
    #         s.append(sum)
    for i in range(0,4):
        #sum = 0
        for j in range(0,4):
            sum = 0
            sum = sum+arr[0+i][0+j]+arr[0+i][1+j]+arr[0+i][2+j]+arr[1+i][1+j]+arr[2+i][0+j]+arr[2+i][1+j]+arr[2+i][2+j]
            s.append(sum)
    a = max(s)
    print(s)
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
