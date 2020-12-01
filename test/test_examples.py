"""test_examples.py - tests for examples.py
"""
import pytest
from unittest.mock import create_autospec, sentinel, call

from examples import power2, fibo, series_calc
import examples


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


@pytest.mark.parametrize('series,n', [
    ('fibonacchi', 3),
    ('fibonacchi', 5),
    ('Fibonacchi', 7),
    ('FIBONACCHI', 5),
])
def test_cals_calls_fibo(series, n, monkeypatch):
    fibo = create_autospec(examples.fibo, return_value=sentinel.fibo)
    power2 = create_autospec(examples.power2, return_value=sentinel.power2)
    monkeypatch.setattr(examples, 'fibo', fibo)
    monkeypatch.setattr(examples, 'power2', power2)

    out = series_calc(series, n)
    assert fibo.call_count == 1
    assert fibo.call_args == call(n)
    assert out == sentinel.fibo
