#!/usr/bin/env python
'''
Beating the stock market

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
'''

def bestBuySell(stock):
    buy, sell, minPrice, maxProfit = [0] * 4

    for i in range(len(stock)):

        if stock[i] < stock[minPrice]:
            minPrice = i

        profit = stock[i] - stock[minPrice]
       
        if profit > maxProfit:
            maxProfit = profit
            sell = i
            buy = minPrice

    return (buy, sell, maxProfit)

if __name__ == '__main__':
    stock = [1, 3, 0, 8, 7, 6, 9]

    buy, sell, profit = bestBuySell(stock)

    print 'Buy on day {}. Sell on day {}. Profit is ${}'.format(buy, sell, profit)
