#!/usr/bin/env python
"""
Given an unsorted array of positive integers.
Find the number of triangles that can be formed with three different array elements as three sides of triangles

Solution:
To form a triangle the only condition that needs to be considered is that the sum of
any two sides should be greater than the third side.

The key to this question is that if we sort the array, and for each value of k
(representing the index of the largest side) find out a pair of indices i and j,
such that sum of sides represented by indices i and j is greater than the third side,
then all indices between i and j-1 will satisfy our condition and hence can be added directly.
This saves us the trouble of identifying all possible triplets.

Runtime: O(n^2)
"""


def number_of_triangles(nums):
    if not nums:
        return 0

    nums.sort()
    total = 0

    for k in range(len(nums) - 1, 1, -1):     # all elements except first 2
        i = 0
        j = k - 1

        # find first (i,j) pair for which triangle is
        # possible with the third side being of length k
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                total += j - i
                j -= 1

            else:
                i += 1

    return total

if __name__ == '__main__':
    assert number_of_triangles([4, 6, 3, 7]) == 3
    assert number_of_triangles([10, 21, 22, 100, 101, 200, 300]) == 6

    print "Test Passed"
