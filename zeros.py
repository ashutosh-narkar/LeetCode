#!/usr/bin/env python
'''
Number of zeros in 100!

Idea:
Number of 5s = Number of 0s
'''

import math

def numZeros(num):
    if not num:
        return 0

    zeros = 0
    while num >= 5:
        zeros += num / 5
        num /= 5

    return zeros

if __name__ == '__main__':
    print numZeros(100)
         
    
