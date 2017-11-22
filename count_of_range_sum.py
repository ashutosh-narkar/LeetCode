#!/usr/bin/env python
"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n^2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.


Solution:
1) First compute the prefix sums: first[m] is the sum of the first m numbers.

2) Then the sum of any subarray nums[i:k] is simply first[k] - first[i].
So we just need to count those where first[k] - first[i] is in [lower,upper]

3) The merge sort based solution counts the answer while doing the merge.
During the merge stage, we have already sorted the left half [start, mid) and right half [mid, end).
We then iterate through the left half with index i.
For each i, we need to find two indices k and j in the right half where

j is the first index satisfy sums[j] - sums[i] > upper and
k is the first index satisfy sums[k] - sums[i] >= lower.

4) Then the number of sums in [lower, upper] is j-k

5) Besides the counting, we also need to actually merge the halves for the sorting.
 Python's 'sorted' method does that. It uses "Timsort" and takes linear time to recognize and
 merge the already sorted halves.


Similar Problems Explanation:
https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs/2

Similar Problems:
count_of_smaller_numbers_after_self.py
reverse_pairs.py
"""


def count_range_sum(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    if not nums:
        return 0

    # First compute the prefix sums
    # sums[i] indicates the sum of numbers from the beginning to index i
    sums = [0] * (len(nums) + 1)

    for i in range(1, len(sums)):
        sums[i] = sums[i - 1] + nums[i - 1]

    return count_while_merge_sort(sums, 0, len(sums), upper, lower)


def count_while_merge_sort(sums, start, end, upper, lower):
    if end - start <= 1:
        return 0

    mid = (start + end) / 2

    count = count_while_merge_sort(sums, start, mid, upper, lower) + count_while_merge_sort(sums, mid, end, upper,
                                                                                            lower)

    j, k = mid, mid

    for i in range(start, mid):
        while k < end and sums[k] - sums[i] < lower:
            k += 1

        while j < end and sums[j] - sums[i] <= upper:
            j += 1

        count += j - k

    sums[start: end] = sorted(sums[start:  end])

    return count
