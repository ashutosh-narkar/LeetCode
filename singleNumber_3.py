#!/usr/bin/env python
'''
Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.

Solution:

1) In the first pass, we XOR all elements in the array, and get the XOR of the two numbers we need to find.
Note that since the two numbers are distinct, so there must be a set bit (that is, the bit with value '1') in the XOR result.
Find out an arbitrary set bit (in below code, the rightmost set bit).

2) In the second pass, we divide all numbers into two groups, one with the rightmost bit set,
another with the rightmost bit unset.
Two different numbers we need to find must fall into the two distinct groups.
XOR numbers in each group, we can find a number in either group.

'''


def single_number(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []

    xor = nums[0]

    #  XOR all elements in the array
    for num in nums[1:]:
        xor = xor ^ num

    # get the rightmost set bit
    bit = xor & ~(xor - 1)

    num1 = 0
    num2 = 0

    # divide all numbers into two groups
    # one with the rightmost bit set and another with the rightmost bit unset
    for num in nums:

        if num & bit:
            num1 = num1 ^ num
        else:
            num2 = num2 ^ num

    return [num1, num2]