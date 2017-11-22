#!/usr/bin/env python
"""
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved.

Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]

Solution:This problem could be divided into 2 sub-problems:

1) function getMax(nums, t):
get t numbers from list nums to form one single maximized sub-list, with relative orders preserved

2) function merge(nums1, nums2):
merge nums1 and nums2 to form one single maximized list, with relative orders preserved

"""


def max_number(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """

    len1 = len(nums1)
    len2 = len(nums2)

    result = []

    for i in range(max(0, k - len2), min(k, len1) + 1):
        left = get_max(nums1, i)
        right = get_max(nums2, k - i)

        tmp = merge(left, right)
        result = max(result, tmp)

    return result


def get_max(nums, t):
    result = []

    for i in range(len(nums)):
        while result and len(result) + len(nums) - i > t and result[-1] < nums[i]:
            result.pop()

        if len(result) < t:
            result.append(nums[i])

    return result


def merge(nums1, nums2):
    ans = []
    while nums1 or nums2:
        if nums1 > nums2:
            ans.append(nums1[0])
            nums1 = nums1[1:]
        else:
            ans.append(nums2[0])
            nums2 = nums2[1:]
    return ans
