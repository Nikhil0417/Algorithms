#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        l = ""
        for j in range(n-1-i):
            l += " "
        for k in range(i+1):
            l += "#"
        print(l)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
