#!/usr/bin/env python
"""
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Solution:
"""


def num_ways(n, k):
    if n == 0:
        return 0

    # there would be k-ways to paint.
    if n == 1:
        return k

    # same[i] means the ith post has the same color with the (i-1)th post
    same = [0] * n

    # diff[i] means the ith post has a different color with the (i-1)th post
    diff = [0] * n

    same[0] = same[1] = k     # no more than two adjacent fence posts have the same color
    diff[0] = k
    diff[1] = k * (k - 1)

    for i in range(2, n):

        # Say for the 3rd fence, if the 1st and 2nd fence we painted the same, the 3rd has to be different
        same[i] = diff[i - 1]

        # Say the 1st and 2nd fence we painted differently, the 3rd fence can we painted differently or
        # with the same color as the 2nd fence
        diff[i] = (k - 1) * same[i - 1] + (k - 1) * diff[i - 1]

    return same[n-1] + diff[n-1]

if __name__ == '__main__':
    print num_ways(3, 2)
