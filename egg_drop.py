#!/usr/bin/env python
"""
Give minimum number of trials to solve an egg drop problem with n eggs and k floors.

Problem Statement: http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/

Solution: There are 2 cases:
1) If the egg breaks after dropping from xth floor, then we only need to check for floors lower than x
with remaining eggs; so the problem reduces to x-1 floors and n-1 eggs

2) If the egg doesn't break after dropping from the xth floor, then we only need to check for floors
higher than x; so the problem reduces to k-x floors and n eggs.


Since we need to minimize the number of trials in worst case, we take the maximum of two cases.
We consider the max of above two cases for every floor and choose the floor which yields minimum number of trials.

Runtime: O(n * k^2)

For 2 eggs and 100 floor: http://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/
"""


def egg_drop(n, k):

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]   # min trials needed

    # for 0 eggs # trails is 0
    for i in range(k + 1):
        dp[0][i] = 0

    # for 0 floors # trails is 0
    for i in range(n + 1):
        dp[i][0] = 0

    # We need one trial for one floor
    for i in range(1, n + 1):
        dp[i][1] = 1

    # We always need j trials for one egg and j floors
    for i in range(1, k + 1):
        dp[1][i] = i

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            for x in range(1, j + 1):
                res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                if res < dp[i][j]:
                    dp[i][j] = res

    return dp[n][k]

if __name__ == '__main__':
    n = 2
    k = 100
    print egg_drop(n, k)
