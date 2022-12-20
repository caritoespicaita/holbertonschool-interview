#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """

    minop = 0
    i = 2

    if n <= 1:
        return minop

    while n > 1:
        if (0 == n % i):
            minop = minop + i
            n = n / i
        else:
            i += 1
    return minop
