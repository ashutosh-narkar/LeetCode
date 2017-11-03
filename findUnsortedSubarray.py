#!/usr/bin/env python
'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


Note:
1. Then length of the input array is in range [1, 10,000].
2. The input array may contain duplicates, so ascending order here means <=.

Solution:

1) Scan from left to right and find the first element which is greater than the next element. (say s)
2) Scan from right to left and find the first element (first in right to left order) which is smaller than the next element
(next in right to left order) (say e)

3) Find the minimum and maximum values in arr[s..e]

4) Keep going left from 's' till an element whose value is less than or equal to min is found

4) Keep going right from 's' till an element whose value is more than or equal to max is found
'''


def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    low = 0
    high = len(nums) - 1

    # go left and find the element whose value is greater than its next element
    while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
        low += 1

    # if low reaches till the end of the list, it means list is already sorted
    if low == len(nums) - 1:
        return 0

    # go right and find the element whose value is smaller than its previous element
    while high > 0 and nums[high] >= nums[high - 1]:
        high -= 1

    # if high reaches the beginning of the list, it means list is already sorted
    if high == 0:
        return 0

    minVal = min(nums[low: high + 1])
    maxVal = max(nums[low: high + 1])

    # Keep going left till a element whose value is less than (or equal to) minVal is found
    while low >= 0 and nums[low] > minVal:
        low -= 1

    # Keep going right till a element whose value is more than (or equal to) maxVal is found
    while high < len(nums) and nums[high] < maxVal:
        high += 1

    return high - low - 1