#!/usr/bin/env python
"""
Given an array arr[], find the maximum j - i such that arr[j] > arr[i].

Examples:

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1


Solution:
1) For an element arr[i], we do not need to consider arr[i] for left index if there is an element smaller
than arr[i] on left side of arr[i].

2) Similarly, if there is a greater element on right side of arr[j] then we do not need to
consider this j for right index.

3) So we construct two auxiliary arrays LMin[] and RMax[] such that LMin[i] holds the smallest element on
left side of arr[i] including arr[i], and RMax[j] holds the greatest element on right side of arr[j] including arr[j].

4) While traversing LMin[] and RMa[] if we see that LMin[i] is greater than RMax[j],
then we must move ahead in LMin[] (or do i++) because all elements on left of LMin[i] are greater than
or equal to LMin[i]. Otherwise we must move ahead in RMax[j] to look for a greater j - i value.
"""


def max_index_diff(nums):

    if not nums:
        return -1

    left_min = [0] * len(nums)
    right_max = [0] * len(nums)

    left_min[0] = nums[0]
    for i in range(1, len(nums)):
        left_min[i] = min(nums[i], left_min[i - 1])

    right_max[-1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        right_max[i] = max(nums[i], right_max[i + 1])

    i, j = 0, 0
    max_diff = -1

    while i < len(left_min) and j < len(right_max):
        if left_min[i] < right_max[j]:
            max_diff = max(max_diff, j - i)
            j += 1

        else:
            i += 1

    return max_diff

if __name__ == '__main__':
    assert max_index_diff([34, 8, 10, 3, 2, 80, 30, 33, 1]) == 6
    assert max_index_diff([9, 2, 3, 4, 5, 6, 7, 8, 18, 0]) == 8
    assert max_index_diff([1, 2, 3, 4, 5, 6]) == 5
    assert max_index_diff([6, 5, 4, 3, 2, 1]) == -1

    print 'Tests Passed'
