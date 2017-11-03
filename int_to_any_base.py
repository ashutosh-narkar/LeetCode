#!/usr/bin/env/python

'''
Convert integer to given base(eg. binary)
The problem comes when we go beyond base 10 since the remainders are themselves 
represented as two-digit decimal numbers.
Instead we need to create a set of digits that can be used to represent those remainders beyond 9
'''

import sys
convertString = "0123456789ABCDEF"

# Similar to excel_sheet
def baseConverter(number, base):
    result = ''

    while number > 0:
        result += convertString[number % base]
        number /= base

    return result[::-1]


def baseConverter_rec(number, base):

    if number < base:
        return convertString[number]

    return baseConverter_rec(number / base, base) + convertString[number % base]


if __name__ == '__main__':
    number = int(sys.argv[1])
    base = int(sys.argv[2])
    res = baseConverter_rec(number, base)
    print 'Number {} Base {} Answer {}'.format(number, base, res)
