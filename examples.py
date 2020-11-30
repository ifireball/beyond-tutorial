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
    else:
        raise RuntimeError(f'Can\'t calculate Fibonacchi value for {n}')


def power2(n):
    """Calculate powers of two

    :param int n: Which number to calculate power of two for
    :return: The Nth power of two
    """
    return 2 ** n


def series_calc(series, n):
    """Calculate values in number series

    :param str series: The number series to calculate values from, can be
                       "fibonacchi" or "powers of two" (case insensitive)
    :param int n:      The position in the series to calculate a value for
    :return: The calculated Nth value
    """
    series = series.lower()
    if series == 'fibonacchi':
        return fibo(n)
    elif series == 'powers of two':
        return power2(n)
    else:
        raise RuntimeError('Unknown series requested')
