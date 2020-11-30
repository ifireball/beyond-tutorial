"""test_examples.py - tests for examples.py
"""
from examples import power2


def test_power2():
    assert power2(0) == 1
    assert power2(1) == 2
    assert power2(2) == 4


def test_fibo():
    assert False, "Please implement tests for fibo()"
