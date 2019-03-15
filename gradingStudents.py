#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    fin = []
    for grade in grades:
        count = 0
        if grade > 37:
            tempgrade = grade
            while tempgrade % 5 != 0:
                tempgrade = tempgrade + 1
                count = count + 1
            if count < 3:
                grade = grade + count
        fin.append(grade)
    return fin

        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
