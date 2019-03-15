#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    flag = True
    solutions = []
    for i in range(1, max(b) + 1):
        for value in a:
            if i % value != 0:
                flag = False
        for value in b:
            if value % i != 0:
                flag = False
        if flag:
            solutions.append(i)
        flag = True
    print(len(solutions))
    return len(solutions)

            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
