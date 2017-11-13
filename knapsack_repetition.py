#!/usr/bin/env python
"""
Given a knapsack weight W and a set of n items with certain value and weight,
we need to calculate minimum amount that could make up this quantity exactly.

This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.
"""


def knapSack_repetition(W, wt, val):

    dp = [0] * (W + 1)
    items = len(wt)

    for i in range(1, W + 1):
        for j in range(items):
            if wt[j] <= i:
                dp[i] = max(dp[i], val[j] + dp[i - wt[j]])

    return dp[W]

if __name__ == '__main__':
    wt = [5, 10, 15]
    val = [10, 30, 20]
    W = 100

    assert knapSack_repetition(W, wt, val) == 300

    wt = [1, 50]
    val = [1, 30]
    W = 100

    assert knapSack_repetition(W, wt, val) == 100

    wt = [1, 3, 4, 5]
    val = [10, 40, 50, 70]
    W = 8

    assert knapSack_repetition(W, wt, val) == 110

    print 'Tests Passed'
