#!/usr/bin/env python
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def threeSumClosest(num, target):

    if not num:
        return

    result = 0
    result_min = float('inf')

    num.sort()

    for i in range(len(num) -2):
        #a + b + c  = target
        desired_sum = target - num[i]

        start = i + 1
        end = len(num) - 1

        while start < end:
            current_sum = num[start] + num[end]

            if current_sum == desired_sum:
                return target

            difference = abs(target - (num[start] + num[end] + num[i]))
            if difference < result_min:
                result_min = difference
                result = num[start] + num[end] + num[i]

            elif current_sum < desired_sum:
                start += 1

            else:
                end -= 1

    return result


if __name__ == '__main__':
    print threeSumClosest([0,0, 0], 1)
