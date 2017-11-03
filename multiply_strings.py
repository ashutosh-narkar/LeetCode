#!/usr/bin/env python
'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

def multiply(num1, num2):

    if not num1 or not num2:
        return '0' 

    result = [0] * (len(num1) + len(num2))

    # reverse for easy calculation
    num1 = num1[::-1]
    num2 = num2[::-1]

    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += int(num1[i]) * int(num2[j])
            result[i + j + 1] += result[i + j] / 10               # carry
            result[i +j] %= 10
    
    # convert list of ints to str
    result = ''.join(map(str, result))

    # remove zeros from right
    result = result.rstrip('0')

    if not result:
        return '0'

    # reverse and return
    return result[::-1]
    
