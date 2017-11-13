#!/usr/bin/env python
"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n
that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.
Return 2. Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]

Solution:

There are two cases to handle:
1) If A[i] + A[j] + A[k] < target, which means the numbers between j and k are all less than target,
because the array is sorted. Then we move the j pointer forward.

2) If A[i] + A[j] + A[k] >= target, we move k pointer backward.
"""


def three_sum_smaller(nums, target):
    if not nums:
        return []

    nums.sort()

    result = 0

    for i in range(len(nums) - 2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            if nums[i] + nums[low] + nums[high] < target:
                result += high - low
                low += 1

            else:
                high -= 1

    return result

if __name__ == '__main__':
    nums = [-2, 0, 1, 3]
    print three_sum_smaller(nums, 2)
