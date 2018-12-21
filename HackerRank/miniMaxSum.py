#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    a = sorted(arr)
    minimum = sum(a[0:4])
    maximum = sum(a[len(arr)-4:])
    print(minimum, maximum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
