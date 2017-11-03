#!/usr/bin.env python
'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4]

Solution:

A[0] <= A[1] >= A[2] <= A[3] >= A[4] <= A[5]
So we could actually observe that there is pattern that
A[even] <= A[odd],
A[odd] >= A[even].

Therefore we could go through the array and check this condition does not hold, just swap.

'''


def wiggleSort(nums):
    if not nums:
        return

    for i in range(len(nums) - 1):
        if i % 2 == 0:
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        else:
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


if __name__ == '__main__':
    input = [3, 5, 2, 1, 6, 4]
    print wiggleSort(input)
