#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2] == 'P':
        if s[:2] == '12':
            hour = '12'
        else:
            hour = str(int(s[0]) + 1) + str(int(s[1]) + 2)
        s = hour + s[2:]
    elif s[:2] == '12':
        s = '00' + s[2:]
    
    return s[:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
