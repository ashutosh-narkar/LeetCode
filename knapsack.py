#!/usr/bin/env python
"""
0-1 Knapsack Problem

Given weights and values of n items, put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.

In other words, given two integer arrays val [0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents knapsack capacity,
find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.

You cannot break an item, either pick the complete item, or don't pick it (0-1 property).

Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.
"""


def knapSack(W, wt, val):
    n = len(val)

    # dp[i][j] indicates the value so far collected by 'i' items having total weight 'j'
    # The first row is all zeros, since if we have 0 items in the knapsack, we have 0 value
    # The first column is all zeros, since if we the knapsack has 0 weight, then the value is 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # if the value of the current item exceeds the current weight, we can't take it.
    # hence value is what we had for the previous items and weight remains the same.
    # if the weight of the current item is less than or equal to the current weight, we can either take it or not
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    print knapSack(W, wt, val)

