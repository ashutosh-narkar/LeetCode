#!/usr/bin/env python
'''
Given an array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.

Explanation:

ones - At any point of time, this variable holds XOR of all the elements which have
appeared "only" once.

twos - At any point of time, this variable holds XOR of all the elements which have
appeared "only" twice.

So if at any point time,

A new number appears - It gets XOR'd to the variable "ones".

A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the
variable "twos".

A number appears for the third time - It gets removed from both "ones" and "twos".

The final answer we want is the value present in "ones" - coz, it holds the unique element.
'''
def single_number(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones
