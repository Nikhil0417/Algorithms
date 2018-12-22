#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    #print(a)
    for i in range(d):
        a.append(a[0])
        b = a.remove(a[0])
        #print(b)
    s = ""
    for j in a:
        s += str(j)+" "
    print(s)
