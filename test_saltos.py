import pytest
from saltos import saltos


def test_salto1():
    arr = [1, 1, 2, 2]
    result = saltos(arr)
    assert result == True

def test_salto2():
    arr = [3, 2, 1, 0, 4]
    result = saltos(arr)
    assert result == False

def test_salto3():
    arr = [3, 3, 1, 2, 0, 1]
    result = saltos(arr)
    assert result == True

def test_salto4():
    arr = [2, 3, 1, 1, 4]
    result = saltos(arr)
    assert result == True