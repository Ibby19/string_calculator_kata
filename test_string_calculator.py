from string_calculator import add,sum_string_numbers
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

def test_random_amount_of_nums():
    assert add('1,2','4,5') == 12
    assert add('1,2','4,5','') == 12

def test_random_delimiter():
    assert add("//;\n3;2") == 5

def test_newline():
    assert add("2\n4,6") == 12

def test_negative_numbers():
    with pytest.raises(ValueError):
        sum_string_numbers('-1,-2')
        sum_string_numbers('-1')
        sum_string_numbers('-1,-2,3')
