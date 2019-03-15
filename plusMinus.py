#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for value in arr:
        if value > 0:
            pos += 1
        elif value < 0:
            neg += 1
        else:
            zer += 1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
