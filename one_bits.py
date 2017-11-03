#!/usr/bin/env python
'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''


#### Same logic as reverse bits
def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
                                            
    mask = 1
    result = 0 
                                                                    
    for i in range(32):
        if n & mask:
            result += 1
                                                                                                                            
        mask <<= 1
                                                                                                                                                    
    return result


def hammingWeight_1(n):
    if not n:
        return 0

    return bin(n).count('1')



def hammingWeight_2(n):
    count = 0
    for i in range(32):
        count += ((n >> i) & 1)

    return count