#!/usr/bin/env python
'''
Beating the stock market

Given an array for which the ith element is price of given stock on day i.
If you were only permitted to buy one share of the stock and sell one share of the
stock, design an algorithm to find best times to buy and sell
'''

def bestBuySell(stock):
    buy, sell, minPrice, maxDiff = [0] * 4

    for i in range(len(stock)):

        if stock[i] < stock[minPrice]:
            minPrice = i

        diff = stock[i] - stock[minPrice]
       
        if diff > maxDiff:
            maxDiff = diff
            sell = i
            buy = minPrice

    return (buy, sell)

if __name__ == '__main__':
    stock = [1, 3, 0, 8, 7, 6, 9]

    buy, sell = bestBuySell(stock)

    print 'Buy on {}. Sell on {}'.format(buy, sell)
