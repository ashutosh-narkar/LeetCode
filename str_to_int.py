#!/usr/bin/env python
'''
Implement atoi to convert a string to an integer.

Requirements for atoi:
1) The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 

2) Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

3) The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

4) If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

5) If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned. 

'''


def atoi(str):

    if not str:
        return 0

    # remove whitespace
    str = str.strip()

    
    # sign
    neg = False
    if str.startswith('-'):
        neg = True
        str = str[1:]

    elif str.startswith('+'):
        str = str[1:]


    result = 0
    i = 0 

    while i < len(str) and '0' <= str[i] <= '9':
        result = result * 10 + (ord(str[i]) - 48)   # ord('0') =  48
        i += 1

    if neg:
        result = -result

    # handle min/ max
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    if result > MAX_INT:
        return MAX_INT

    if result < MIN_INT:
        return MIN_INT

    return result
