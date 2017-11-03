#!/usr/bin/env python
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
'''

# @param num, a list of integer
# @return an integer


def rob(num):

    if not num:
        return 0

    # one house
    if len(num) == 1:
        return num[0]

    # 2 houses
    if len(num) == 2:
        return max(num[0], num[1])

    # 3 houses - 1st and 3rd can be robbed  OR only 2nd 
    if len(num) == 3:
        return max(num[0] + num[2], num[1])

    # update cost upto 3rd house
    num[2] += num[0]

    # Starting from the 4th house, we need to consider the n-2 and n-3 since we know n-1 is not possible.
    for i in range(3, len(num)):
        num[i] += max(num[i - 2], num[i - 3])

    # return last or second last value
    return max(num[-1], num[-2])
