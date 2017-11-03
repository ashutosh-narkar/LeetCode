#!/usr/bin/env python
'''
Given a non negative integer number 'num'. For every numbers i in the range 0 <= i <= num,
calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].


Solution:
For number 2(10), 4(100), 8(1000), 16(10000), ..., the number of 1's is 1.
Any other number can be converted to be 2 ^ m + x.

For example, 9 = 8 + 1, 10 = 8 + 2. The number of 1's for any other number is 1 + # of 1's in x.

Number        # of Ones
1               1
2               1
3 (2 + 1)       2
4               1
5 (4 + 1)       2
6 (4 + 2)       2
7 (4 + 3)       3
8               1
9 (8 + 1)       2
10 (8  + 2)     2
'''


def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    if not num:
        return [0]

    pow = 1  # 2^0
    p = 1  # p tracks the index for number x

    result = [0] * (num + 1)

    for i in range(1, num + 1):
        if i == pow:
            result[i] = 1  # for all powers of 2, # ones = 1
            pow <<= 1  # go to the next power of 2
            p = 1  # reset the index

        else:
            result[i] = 1 + result[p]
            p += 1

    return result