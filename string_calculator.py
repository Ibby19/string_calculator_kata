import re

delimiter = ','

def add(*num):
    """ This function returns 0 if an empty string is passed. 
    It also splits a string and turns it into an integer
    then adds the strings"""
    total = 0

    for numbers in num:
        if numbers != "":
            numbers = second_delimter(numbers)
            total += sum(map(int, numbers.split(delimiter)))
    return total

def second_delimter(numbers):
    """ This function splits a string by the new line delimiter"""
    return numbers.replace("\n", delimiter)