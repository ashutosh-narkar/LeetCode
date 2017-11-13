#!/usr/bin/env python
"""
Given an array of integers, find two non-overlapping contiguous sub-arrays such that
the absolute difference between the sum of two sub-arrays is maximum.

For example,

Input: [-2, -3, 4, -1, -2, 1, 5, -3]
Output: 12
Two subarrays are [-2, -3] and [4, -1, -2, 1, 5]

Input: [2, -1, -2, 1, -4, 2, 8]
Output: 16
Two subarrays are [-1, -2, 1, -4] and [2, 8]

Solution: The idea is for each index i in the nums[0 ... n -1], we maintain the following four arrays:
leftMax[] : An element leftMax[i] of this
            array stores the maximum value
            in subarray arr[0..i]

leftMin[] : An element leftMin[i] of this
            array stores the minimum value
            in subarray arr[0..i]

rightMax[] : An element rightMax[i] of this
             array stores the maximum value
             in subarray arr[i+1..n-1]

rightMin[] : An element rightMin[i] of this
             array stores the minimum value
             in subarray arr[i+1..n-1]

The above four arrays can be found using Kadane's algorithm

For each index i, take maximum of

1) abs(max sum subarray that lies in arr[0...i] - min sum subarray that lies in arr[i + 1...n - 1])
2) abs(min sum subarray that lies in arr[0...i] - max sum subarray that lies in arr[i + 1...n - 1])


Runtime: O(n)
"""


def max_left_subarray_sum(nums):

    result = [0] * len(nums)

    result[0] = nums[0]
    current_max = nums[0]
    overall_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(current_max + nums[i], nums[i])
        overall_max = max(overall_max, current_max)
        result[i] = overall_max

    return result


def max_right_subarray_sum(nums):
    result = [0] * len(nums)

    result[len(nums) - 1] = nums[-1]
    current_max = nums[-1]
    overall_max = nums[-1]

    for i in range(len(nums) - 2, -1, -1):
        current_max = max(current_max + nums[i], nums[i])
        overall_max = max(overall_max, current_max)
        result[i] = overall_max

    return result


def find_max_abs_diff(nums):
    if not nums:
        return 0

    # left max
    left_max = max_left_subarray_sum(nums)

    # right max
    right_max = max_right_subarray_sum(nums)

    # invert the array to find the left and right min
    invert_array = [0] * len(nums)
    for i in range(len(nums)):
        invert_array[i] = -nums[i]

    # left min
    left_min = max_left_subarray_sum(invert_array)
    for i in range(len(left_min)):
        left_min[i] = -left_min[i]

    # right min
    right_min = max_right_subarray_sum(invert_array)
    for i in range(len(right_min)):
        right_min[i] = -right_min[i]

    result = float('-inf')

    for i in range(len(nums) - 1):
        temp = max(abs(left_max[i] - right_min[i + 1]), abs(left_min[i] - right_max[i + 1]))

        if temp > result:
            result = temp

    return result

if __name__ == '__main__':
    data = [-2, -3, 4, -1, -2, 1, 5, -3]
    assert find_max_abs_diff(data) == 12

    data = [2, -1, -2, 1, -4, 2, 8]
    assert find_max_abs_diff(data) == 16

    print "Tests passed"
