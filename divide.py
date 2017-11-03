#!/usr/bin/env python
'''
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.

Analysis:
We can keep subtract divisor from dividend until dividend is smaller than 0, then count the subtract numbers. 
But it will take a very long time if the divisor is very small compared to dividend.


1) We shift the divisor left till it exceeds  dividend 
2) Than we can add the shifted value to the result and subtract the shifted divisor from dividend.
Keep doing this until dividend is smaller than divisor.

The complexity is O(log n) ??

'''
def divide(dividend, divisor):

    # Remember the sign
    negative = (dividend < 0) ^ (divisor < 0)

    dividend, divisor = abs(dividend), abs(divisor)

    # Return if nothing to divide
    if dividend < divisor:
        return 0

    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1

    if negative:
        res = -res

    return min(max(-2 **31, res), 2 ** 31 -1)

        
