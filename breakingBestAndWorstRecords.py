#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    most = scores[0]
    mostcount = 0
    least = scores[0]
    leastcount = 0
    for value in scores:
        if value > most:
            most = value
            mostcount += 1
        if value < least:
            least = value
            leastcount += 1
    return mostcount, leastcount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
