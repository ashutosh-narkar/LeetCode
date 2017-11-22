#!/usr/bin/env python
"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that
any number in range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.


Explanation: http://buttercola.blogspot.com/2016/06/leetcode-330-patching-array.html
"""


def min_patches(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """

    patch = 0
    maxreach = 0

    i = 0

    while maxreach < n:
        # current number is smaller or equal to the sum we want to reach
        if i < len(nums) and nums[i] <= maxreach + 1:
            maxreach += nums[i]  # update the max sum so far
            i += 1

        # current number exceeds the maxreach, it means we need to
        # add a number to reach the maxreach
        else:
            maxreach += maxreach + 1
            patch += 1

    return patch
