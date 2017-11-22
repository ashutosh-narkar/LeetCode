#!/usr/bin/env python
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]


Solution:

The key is 3 states and 5 edges for state transition. 3 states are notHold (stock), hold (stock), and notHold_cooldown. The initial values of the latter two are negative infinity since they are meaningless, i.e. you won't hold stocks at first and there's no cooldown at first. The 5 edges:

hold -----do nothing----->hold

hold -----sell----->notHold_cooldown

notHold -----do nothing -----> notHold

notHold -----buy-----> hold

notHold_cooldown -----do nothing----->notHold

'''


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    if not prices or len(prices) == 1:
        return 0

    notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')

    for p in prices:
        hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p

    return max(notHold, notHold_cooldown)