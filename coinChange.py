#!/usr/bin/env python
'''
You are given coins of different denominations and a total amount of money amount.

Write a function to compute the fewest number of coins that you need to make up that amount.

If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''


def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    if not coins:
        return 0

    # Let dp[v] to be the minimum number of coins required to get the amount v
    dp = [float('Inf')] * (amount + 1)

    # number of coins to make $0
    dp[0] = 0

    for coin in coins:
        for i in range(1, amount + 1):
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] >= float('Inf'):
        return -1

    return dp[amount]