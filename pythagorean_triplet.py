#!/usr/bin/env python
"""
Given an array of integers, write a function that returns true if there is a triplet (a, b, c)
that satisfies a2 + b2 = c2.

Example:

Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.

Solution:
For a Pythagorean triplet: c^2 = a^2 + b^2

1) Square every element in the array
2) Sort array in increasing order
3) Set the last element 'c' to the last element in the array
4) Now find two numbers 'a' and 'b' such that a + b = c. This is similar to 3 sum.

Runtime: O(n^2)
"""

def is_triplet(nums):
    if not nums:
        return False

    for i, num in enumerate(nums):
        nums[i] = num * num

    nums.sort()

    for i in range(len(nums) - 1, 1, -1):     # all elements except first 2
        low = 0
        high = i - 1

        while low < high:
            if nums[low] + nums[high] == nums[i]:
                return True

            elif nums[low] + nums[high] < nums[i]:
                low += 1

            else:
                high -= 1

    return False


if __name__ == '__main__':
    assert is_triplet([3, 1, 4, 6, 5]) == True

    assert is_triplet([10, 4, 6, 12, 5]) == False

    print 'Tests Passed'
