#!/usr/bin/env python
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''


# Solution 1: 1 pass Binary Search
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return -1

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) / 2

        if nums[mid] == target:
            return mid

        # everything from low to mid is sorted
        elif nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:  # target cannot be = nums[mid]
                high = mid - 1
            else:
                low = mid + 1

        # everything from mid to high is sorted
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# Solution 2: 2 pass Binary Search

def find_num(numbers, val):
    '''
    Find the given val in numbers list
    '''
    pivot = find_pivot(numbers)
    if pivot == -1:
        return binarySearch(numbers, val, 0, len(numbers) - 1)

    # If we found a pivot, then first compare with pivot and then
    # search in two subarrays around pivot
    if numbers[pivot] == val:
        return pivot
    elif val >= numbers[0]:
        return binarySearch(numbers, val, 0, pivot - 1)
    else:
        return binarySearch(numbers, val, pivot + 1, len(numbers) - 1)


def binarySearch(numbers, val, low, high):
    while low <= high:
        mid = low + (high - low) / 2
        if numbers[mid] == val:
            return mid
        elif val < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_pivot(numbers):
    '''
    Function to get pivot. For array 3, 4, 5, 6, 1, 2 it will
    return 3 (index of 6). If array is not rotated at all, then it returns -1 */
    '''
    low = 0
    high = len(numbers) - 1

    # Notice NO '='
    while low < high:
        mid = low + (high - low) / 2

        if numbers[mid] > numbers[mid + 1]:
            return mid
        elif numbers[mid] < numbers[mid - 1]:
            return mid - 1

        elif numbers[low] > numbers[mid]:
            high = mid - 1

        ##############################
        # Add this condition if duplicates are allowed in array
        elif numbers[low] == numbers[mid]:
            low += 1

        ##############################


        else:
            low = mid + 1

    return -1


def main():
    print find_num([3, 4, 5, 6, 1, 2], 1)


if __name__ == '__main__':
    main()