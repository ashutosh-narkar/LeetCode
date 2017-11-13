#!/usr/bin/env python
"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""


def is_strobogrammatic(num):
    if not num:
        return False

    nums = dict()
    nums['0'] = '0'
    nums['1'] = '1'
    nums['6'] = '9'
    nums['8'] = '8'
    nums['9'] = '6'

    l = 0
    r = len(num) - 1

    while l <= r:
        if num[l] not in nums:
            return False

        if nums[num[l]] != num[r]:
            return False

        l += 1
        r -= 1

    return True

if __name__ == '__main__':
    assert is_strobogrammatic('69') == True
    assert is_strobogrammatic('88') == True
    assert is_strobogrammatic('818') == True
    assert is_strobogrammatic('919') == False

    print 'Tests Passed'
