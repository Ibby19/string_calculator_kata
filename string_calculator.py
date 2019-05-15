import re

delimiter = ','

def add(*num):
    """ This function returns 0 if an empty string is passed. 
    It also splits a string and turns it into an integer
    then adds the strings"""
    total = 0

    for numbers in num:
        if numbers != "":
            numbers = any_delimiter(numbers)
            numbers = second_delimter(numbers)
            total += sum(map(int, numbers.split(delimiter)))
    return total
        
def second_delimter(numbers):
    """ This function splits a string by the new line delimiter"""
    return numbers.replace("\n", delimiter)

def any_delimiter(numbers):
    if re.match('//.{1}\n', numbers):
        d_separator = numbers[2]
        numbers = numbers[4:]
        numbers = numbers.replace(d_separator,delimiter)
    return numbers

def sum_string_numbers(string):
    """ This function splits the string by a delimiter
    then it checks if the numbers in the string are negative"""
    numbers = map(int, string.split(','))
    invalid_number(numbers)
    return sum(numbers)

def invalid_number(numbers):
    """ This function checks if a number in the string is negative
    then returns a value error"""
    if any(number < 0 for number in numbers):
        raise ValueError ("You can't use a negative number")