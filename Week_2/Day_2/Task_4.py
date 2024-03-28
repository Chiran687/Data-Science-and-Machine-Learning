# Create a program that checks if a given 3x3 matrix forms a magic square.

"""A magic square is a square matrix where the sums of the numbers in each row, column, and both main diagonals are the same.
Ask the user to input a 3x3 matrix (nine integer values).
Check and print whether the given matrix forms a magic square.
Handle cases where the input matrix is not of size 3x3 or contains non-integer values."""

import numpy as np


def magic_checker(matrix):

    print(matrix)

    n = len(matrix)
    sum1 = 0
    sum2 = 0

    for i in range(n):
        sum1 += matrix[i][i]
        sum2 += matrix[i][n-i-1]

    if not (sum1 == sum2):
        return False

    for i in range(n):
        sumr = 0
        sumc = 0

        for x in range(n):
            sumr += matrix[i][x]
            sumc += matrix[x][i]
        if not (sumr == sumc == sum1):
            return False

    return True


matrix = np.random.randint(1, 9, size=(3, 3))

if (magic_checker(matrix)):
    print("Magic square")
else:
    print("Not Magic square")
