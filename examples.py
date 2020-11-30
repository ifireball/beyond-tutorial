#!/usr/bin/env python3
"""examples.py - Simple Python example functions for teaching PyTest
"""


def fibo(n):
    """Calculate Fibonacchi numbers

    :param int n: Which position in the series to return the number for
    :returns: The Nth number in the Fibonacchi series
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibo(n - 1) + fibo(n - 2)


def power2(n):
    """Calculate powers of two

    :param int n: Which number to calculate power of two for
    :return: The Nth power of two
    """
    return 2 ** n
