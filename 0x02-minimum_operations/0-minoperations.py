#!/usr/bin/python3
'''
Given a number n, write a method that calculates
the fewest number of operations needed to result in
exactly n H characters in the file.
'''


def minOperations(n: int) -> int:
    """minOperations is a method that calculates
    the fewest number of operations needed to result
    in exactly n H characters
    Args:
        n (int): amount of H
    Return:
        minimum number of operations (an integer)
    """
    minOps = 0
    copied = 0
    numOfH = 1
    while numOfH < n:
        # copy and paste only if n is divisible by numOfH
        if n % numOfH == 0:
            copied = numOfH
            numOfH *= 2
            minOps += 2
        else:
            # just paste until reaching n
            numOfH += copied
            minOps += 1

    return minOps
