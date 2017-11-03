#!/usr/bin/env python
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Runtime: O(n)

Solution: First turn the input into a set of numbers.
That takes O(n) and then we can ask in O(1) whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set),
then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set.
The length of the streak is then simply y-x and we update our global best with that.
Since we check each streak only once, this is overall O(n).
"""


def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    nums = set(nums)
    max_len = 0

    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1

            max_len = max(max_len, y - x)

    return max_len

if __name__ == '__main__':

    nums = [100, 300, 1, 4, 0, 6, 400, 2, 3, 401, 402, 5]

    print 'Length of longest consecutive elements sequence in {} is {}'.format(nums, longestConsecutive(nums))
