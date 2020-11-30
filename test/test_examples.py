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


@pytest.mark.parametrize('n,expected', [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (0, RuntimeError),
    (-1, RuntimeError),
])
def test_fibo(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            fibo(n)
    else:
        assert fibo(n) == expected
