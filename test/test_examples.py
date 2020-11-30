"""test_examples.py - tests for examples.py
"""
import pytest

from examples import power2, fibo


@pytest.mark.parametrize('n,expected', [
    (0, 1),
    (1, 2),
    (2, 4),
    (3, 8),
    (4, 16),
    (5, 32),
    (10, 1024),
    (16, 65536),
])
def test_power2(n, expected):
    assert power2(n) == expected


def test_fibo():
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8
