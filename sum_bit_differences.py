#!/usr/bin/env python
"""
Given an integer array of n integers, find sum of bit differences in all pairs that can be formed from array elements.
Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.

For example, bit difference for 2 and 7 is 2.
Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).

Examples:

Input: arr[] = {1, 2}
Output: 4
All pairs in array are (1, 1), (1, 2)
                       (2, 1), (2, 2)
Sum of bit differences = 0 + 2 +
                         2 + 0
                      = 4

Input:  arr[] = {1, 3, 5}
Output: 8
All pairs in array are (1, 1), (1, 3), (1, 5)
                       (3, 1), (3, 3) (3, 5),
                       (5, 1), (5, 3), (5, 5)
Sum of bit differences =  0 + 1 + 1 +
                          1 + 0 + 2 +
                          1 + 2 + 0
                       = 8

Solution:

All numbers are represented using 32 bits (or some fixed number of bits). The idea is to count differences at
individual bit positions. We traverse from 0 to 31 and count numbers with i'th bit set.

Let this count be 'count'. There would be "n-count" numbers with i'th bit not set.
So count of differences at i'th bit would be "count * (n-count) * 2".

Runtime:O(n)
"""


def sum_bit_differences(nums):
    if not nums:
        return 0

    result = 0

    # traverse over all bits
    for i in range(32):

        # count number of elements with i'th bit set
        count = 0
        for num in nums:
            if num & (1 << i):
                count += 1

        # We multiply by 2 since (x, y) and (y, x) are both pairs
        result += count * (len(nums) - count) * 2

    return result

if __name__ == '__main__':
    print sum_bit_differences([1, 2])
    print sum_bit_differences([1, 3, 5])
