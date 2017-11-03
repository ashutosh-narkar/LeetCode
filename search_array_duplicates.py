#!/usr/bin/env python
"""
Given a sorted array with duplicates, find how many times a given element occurs

eg. nums = [1,2,3,4,5,5,6,7,7] ,  target = 5
Output = 2
"""


def count_helper(sorted_arr, element, searchFirstIndex):
    low = 0
    high = len(sorted_arr) - 1

    result = -1   # if the element is not found return -1

    while low <= high:

        mid = low + (high - low) / 2

        if sorted_arr[mid] == element:

            # set the result to the index
            result = mid

            # to search the first index, we need to search towards the left (ie lower indices)
            # to search the last index, we need to search towards the right (ie higher indices)
            if searchFirstIndex:
                high = mid - 1
            else:
                low = mid + 1

        elif sorted_arr[mid] < element:
            low = mid + 1

        else:
            high = mid - 1

    return result


def count(sorted_arr, element):
    if not sorted_arr:
        return 0

    lowest_index = count_helper(sorted_arr, element, True)

    # element not found
    if lowest_index == -1:
        return 0

    else:
        highest_index = count_helper(sorted_arr, element, False)

        return highest_index - lowest_index + 1


if __name__ == '__main__':
    nums = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
    target = 5

    print count(nums, target)