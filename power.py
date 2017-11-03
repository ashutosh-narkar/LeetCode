#!/usr/bin/env python
'''
Calculate the base to the exponent, that is, base^exponent
'''

import sys


def main():
    '''
     Given base and exponent, calculate base to the exponent
    '''
    base = float(sys.argv[1])
    exp = float(sys.argv[2])

    res = _calculate_power_log(base, exp)
    print 'Recursive: Base {} exponent {} result {}'.format(base, exp, res)

    res = _calculate_power_log_2(base, exp)
    print 'Iterative: Base {} exponent {} result {}'.format(base, exp, res)

def _calculate_power(base, exp):
    '''
    Return base raised to exponent
    '''
    if exp == 0:
        return 1

    elif exp == 1:
        return base

    else:
        result = 1
        while exp > 0:
            result *= base
            exp -= 1
        return result


def _calculate_power_rec(base, exp):
    '''
    Return base raised to exponent using a recursive
    approach
    '''
    if exp == 0:
        return 1

    elif exp == 1:
        return base

    else:
        return  base * _calculate_power_rec(base, exp - 1)


def _calculate_power_log(base, exp):
    '''
    Use the Exponentiation by Squaring method, to find power in O(logn)
    '''

    if exp < 0:
        return _calculate_power_log(1/float(base), -exp)   

    elif exp == 0:
        return 1

    elif exp == 1:
        return base

    elif exp % 2:
        return base * _calculate_power_log(base*base, (exp-1)/2)

    elif not exp % 2:
        return _calculate_power_log(base*base, exp/2)


def _calculate_power_log_2(base, exp):
    
    if exp == 0:
        return 1
   
    if exp == 1:
        return base

    if exp < 0:
        base = 1 / float(base)
        exp = -exp

    result = 1
    while exp > 0:
        if exp % 2:
            result *= base
            exp -= 1
 
        base *= base
        exp = exp / 2 

    return result

    

if __name__ == '__main__':
    main()
