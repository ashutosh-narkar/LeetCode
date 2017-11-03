#!/usr/bin/env python
'''
Reverse an integer
'''
import sys

def reverse(x):

    neg = False
    if x < 0:
        neg = True
        x = -x

    res = 0
    p = x

    while (p > 0):
        mod = p % 10
        res = res * 10 + mod

        # if res overflows
        if res > 2 ** 31:
            return 0

        p /= 10
    
    if neg:
        return -res
    return res


if __name__ == '__main__':
    data  = int(sys.argv[1])
    print 'Reverse of {} is {}'.format(data, reverse(data))    
