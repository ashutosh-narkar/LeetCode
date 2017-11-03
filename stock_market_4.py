#!/usr/bin/env python
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

def maxProfit(k, prices):

    if k == 0 or not prices or len(prices) < 2:
	return 0

	
    # In this case, we can perform as many transactions as we want. So same as Part2
    if k > len(prices) / 2:
	return quickSolve(prices)



    balance = [float('-inf')] * (k + 1)    # the balance with exactly j transactions with item 0 to i
    profit = [0] * (k + 1)                 # the profit with exactly j transactions with item 0 to i

    

    for i in range(len(prices)):
	for j in range(1, k + 1):
	    balance[j] = max(balance[j], profit[j -1] - prices[i]) # if we decide to buy today, then balance =  profit made upto the previous transactions - price of stock today
	    profit[j] = max(profit[j], balance[j] + prices[i])     # if we decide to sell today, then profit = current balance + price of stock today


    return profit[-1]

            

def quickSolve(prices):

    profit  = 0

    for i in range(len(prices) - 1):
        diff = prices[i + 1] -  prices[i]
        if diff > 0:
            profit += diff

    return profit




