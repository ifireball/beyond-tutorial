"""test_examples.py - tests for examples.py
"""
from examples import power2, fibo


def test_power2():
    assert power2(0) == 1
    assert power2(1) == 2
    assert power2(2) == 4


def test_fibo():
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8
