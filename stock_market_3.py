#!/usr/bin/env python
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Solution:
Step 1: We compute the forward max profit and save it. Forward max profit means for each day i, 
we want to know the max profit we can make no later than this day. Note that we only need to consider 1 transaction

Step 2: We compute the reverse max profit and save it. Reverse max profit means for each day i, 
we want to know the max profit we can make for days later i.

Step 3: The max profit is the sum of max profit before day i and after day i.

'''
def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0


    # Step 1
    left = [0]      # profit is 0 on first day
    minPrice = 0    # assume price of stock is min on day 0 ie. 1st day


    for i in range(1, len(prices)):
        # get profit by calculating difference between
        # today's stock price and price of stock on minPrice day
        if prices[i] < prices[minPrice]:
            minPrice = i

        profit = max(prices[i] - prices[minPrice], left[i - 1])
        left.append(profit)



    # Step 2
    right = [0] * len(prices)     # profit is 0 on last day. We initialize the array to avoid 'list.insert' in the loop
    maxPrice = len(prices) - 1    # assume price of stock is max on last day

    for i in reversed(range(len(prices) - 1)):
        if prices[i] > prices[maxPrice]:
            maxPrice = i

        profit = max(prices[maxPrice] - prices[i], right[i + 1])
        right[i] = profit


    # Step 3
    profit = 0
    for i in range(len(prices)):
        profit = max(profit, left[i] + right[i])

    return profit


if __name__ == '__main__':
    input = [1,2,4,2,5,7,2,4,9]
    print 'Max profit using 2 transactions is {}'.format(maxProfit(input))
        
