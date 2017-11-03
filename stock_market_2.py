#!/usr/bin/env python
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Solution:
This problem can be viewed as finding all ascending sequences. 
For example, given {5, 1, 2, 3, 4}, buy at 1 & sell at 4 is the same
as buy at 1 &sell at 2 & buy at 2& sell at 3 & buy at 3 & sell at 4.

We can scan the array once, and find all pairs of elements that are in ascending order.
'''


def maxProfit(prices):

    if not prices or len(prices) == 1:
        return 0

    profit = 0
    for i in range(len(prices) - 1):

        diff = prices[i + 1] - prices[i]

        if diff > 0:
            profit += diff

    return profit

if __name__ == '__main__':
    input = [1,2,4,2,5,7,2,4,9]
    print maxProfit(input)
