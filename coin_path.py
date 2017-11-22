#!/usr/bin/env python
"""
Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B.
The integer B denotes that from any place (suppose the index is i) in the array A,
you can jump to any one of the place in the array A indexed i+1, i+2, ..., i+B
if this place can be jumped to. Also, if you step on the index i, you have to pay Ai coins.
If Ai is -1, it means you can't jump to the place indexed i in the array.

Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the
minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should
take to get to the place indexed N using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed N then you need to return an empty array.

Example 1:

Input: [1,2,4,-1,2], 2
Output: [1,3,5]


Example 2:

Input: [1,2,4,-1,2], 1
Output: []


Solution: This is a classic DP problem. dp[k] (starting from k = 0) is the minimum coins from Ak+1 to An,
and pos[k] is the next place to jump from Ak+1.

If working backward from dp[n-1] to dp[0], and considering smaller index first, i.e. i+1 to i+B,
there is no need to worry about lexicographical order.
pos[k] always holds the lexicographically smallest path from k to n-1, i.e. from Ak+1 to An.

For Proof see https://discuss.leetcode.com/topic/98399/c-dp-o-nb-time-o-n-space

"""


def cheapest_jump(nums, b):

    if not nums:
        return []

    result = []

    dp = [float('inf')] * len(nums)

    dp[-1] = nums[-1]

    pos = [-1] * len(nums)

    # working backward
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] == -1:
            continue

        for j in range(i + 1, min(i + b + 1, len(nums))):
            if dp[j] == float('inf'):
                continue

            dp[i] = dp[j] + nums[i]
            pos[i] = j

    # cannot jump to An
    if dp[0] == float('inf'):
        return []

    k = 0
    while k != -1:
        result.append(k + 1)
        k = pos[k]

    return result

if __name__ == '__main__':
    assert cheapest_jump([1,2,4,-1,2], 2) == [1, 3, 5]

    assert cheapest_jump([1,2,4,-1,2], 1) == []

    print "Tests Passed"
