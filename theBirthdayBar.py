#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    if len(s) == 0:
        count =  0
    elif len(s) == 1 and m == 1:
        return int(s[0] == d)
    elif len(s) == 2 and m == 2:
        count = int(s[0] + s[1] == d)
    elif len(s) == 2 and m == 1:
        count = int(s[0] == d) + int(s[1] == d)
    
    for i in range(0, len(s) - m + 1):
        sum = 0
        for j in range(0, m):
            sum += s[i + j]
        if sum == d:
            count += 1
    print(count)
    return count





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
