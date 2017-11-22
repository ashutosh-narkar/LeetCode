#!/usr/bin/env python
"""
Given an array of n positive integers that represent lengths.
Find out the maximum possible area whose four sides are picked from given array.
Note that a rectangle can only be formed if there are two pairs of equal values in given array.


Examples:

Input : arr[] = {2, 1, 2, 5, 4, 4}
Output : 8
Explanation : Dimension will be 4 * 2

Input : arr[] = {2, 1, 3, 5, 4, 4}
Output : 0
Explanation : No rectangle possible

Solution: The idea is to insert all first occurrences of elements in a hash set.
For second occurrences, keep track of maximum two values.

Time Complexity : O(n)
"""


def find_area(nums):
    if not nums:
        return 0

    seen = set()

    first, second = 0, 0

    for num in nums:

        # first occurrence
        if num not in seen:
            seen.add(num)
            continue

        if num > first:
            second = first
            first = num

        elif num > second:
            second = num

    return first * second

if __name__ == '__main__':
    assert find_area([4, 2, 1, 4, 6, 6, 2, 5]) == 24
    assert find_area([2, 1, 2, 5, 4, 4]) == 8
    assert  find_area([2, 1, 3, 5, 4, 4]) == 0

    print 'Tests Passed'
