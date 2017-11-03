#!/usr/bin/env python
'''
Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].
Examples:

Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56}
Output: 30 39 42 45

Note that if the element is present in array, then it should not be in output, only the other closest elements are required.

Runtime:  O(Logn + k)
'''


def getClosest(nums, k, val):

    if not nums:
        return

    pivot = getPivot(nums, val)

    # since we do not want the number itself in the final result
    left = pivot if nums[pivot] != val else pivot - 1
    right = left + 1

    count = 0
    result = []

    # Compare elements on left and right of crossover
    # point to find the k closest elements

    while left >= 0 and right < len(nums) and count < k:
        diff1 = abs(val - nums[left])
        # since we do not want the number itself in the final result
        if diff1 == 0:
            left -= 1
            continue

        diff2 = abs(val - nums[right])
        # since we do not want the number itself in the final result
        if diff2 == 0:
            right += 1
            continue

        if diff1 == diff2:
            # can only add one num 
            if count == k - 1:
                result.append(nums[left])
                count += 1
                return result
    
            else:
                result.append(nums[left])
                result.append(nums[right])
                left -= 1
                right += 1
                count += 2

        elif diff1 > diff2:
            result.append(nums[right])
            right += 1
            count += 1

        else:
            result.append(nums[left])
            left -= 1
            count += 1

    if count == k:
        return result

    if left < 0:
        while count < k and right < len(nums):
            result.append(nums[right])
            right += 1

    if right == len(nums):
        while count < k and left >= 0:
            result.append(nums[left])
            left -= 1

    return result


def getPivot(nums, val):

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) / 2

        if nums[mid] == val:
            return mid

        elif nums[mid] < val < nums[mid + 1]:
            return mid

        elif nums[mid] < val:
            low = mid + 1

        else:
            high = mid - 1


if __name__ == '__main__':

    input = [12, 16, 22, 31, 31, 35, 40, 42, 45, 48, 50, 53, 55, 56]
    print getClosest(input, 4, 35)


 
