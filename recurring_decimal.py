#!/usr/bin/env python
'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

Solution:
Use HashMap to store a remainder and its associated index while doing the division
so that whenever a same remainder comes up, we know there is a repeating fractional part.
'''

def fractionToDecimal(numerator, denominator):

    if numerator == 0:
        return '0'

    res = ''

    # sign **brackets are necessary
    if (numerator > 0) ^ (denominator > 0):
        res = '-'

       
    numerator, denominator = abs(numerator), abs(denominator)
 
    # integral part    
    res += str(numerator/ denominator)

    numerator %= denominator

    # number is divisible
    if numerator == 0:
        return res


    # fractional part
    res += '.'


    index = {}
    index[numerator] = len(res)

    while numerator != 0:
        numerator *= 10
        res += str(numerator / denominator)
        numerator %= denominator

        if numerator not in index:
            index[numerator] = len(res)

        # already seen this remainder
        else:
            pos = index[numerator]
            res = res[: pos] + '(' + res[pos:] + ')'
            break
            
    return res

if __name__ == '__main__':
    print fractionToDecimal(-50, 8)
    

