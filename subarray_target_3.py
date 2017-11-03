#!/usr/bin/env python
'''
Given an array nums and a target value k, find the maximum length of a
subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (Because the subarray [-1, 2] sums to 1 and is the longest)
'''

def maxSubArrayLen(nums, k):

    if not nums:
        return 0

    max_len = 0
    sum = 0
    d = {}

    for i in range(len(nums)):
        sum += nums[i]

        if sum == k:
            max_len = max(max_len, i + 1)

        if (sum - k) in d:
            max_len = max(max_len, i - d[sum - k])

        # Only keep the smallest index
        if sum not in d:
            d[sum] = i

    return max_len


if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    k = 3

    assert maxSubArrayLen(nums, k) == 4

    nums = [-2, -1, 2, 1]
    k = 1

    assert maxSubArrayLen(nums, k) == 2

    print "Test passed"