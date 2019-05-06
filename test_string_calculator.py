from string_1 import *
import pytest

def test_add_and_empty_string():
    assert add('') == 0

def test_add_int_strings():
    assert add('1','2') == 3
    assert add('5,5') == 10
    assert add('15','15') == 30

def test_return_number():
    assert add('0') == 0
    assert add('5') == 5
    assert add('10') == 10

def test_sum_multiple_numbers():
    assert add('10,20,30') == 60
    assert add('5,5,5,5') == 20
    assert add('2,4,6') == 12