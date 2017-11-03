#!/usr/bin/env python
'''
Note: This is an extension of House Robber 1.

After robbing those houses on that street, the thief has found himself a new place for his thievery
so that he will not get too much attention. This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.

Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Solution:
Suppose there are n houses, since house 0 and n - 1 are now neighbors, we cannot rob them together and
thus the solution is now the maximum of

Rob houses 0 to n - 2;
Rob houses 1 to n - 1.
'''


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    return max(robber(nums, 0, len(nums) - 2), robber(nums, 1, len(nums) - 1))


def robber(nums, l, r):
    pre = 0
    cur = 0

    for i in range(l, r + 1):
        temp = max(pre + nums[i], cur)
        pre = cur
        cur = temp

    return cur
