#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    lastAnswer = 0
    l = []
    s = []
    for i in range(n):
        s.append([])
    #print(n, queries)
    for i in range(len(queries)):
        bit=queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        #print(bit,x,y)
        if bit==1:
            a = (x^lastAnswer)%n
            #print(a)
            s[a].append(y)
            #print(s0)
        elif bit==2:
            a = (x^lastAnswer)%n
            lastAnswer = s[a][y%(len(s[a]))]
            print(lastAnswer)
            l.append(lastAnswer)
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
