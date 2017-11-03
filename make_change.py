#!/usr/bin/env python
'''
Make change using the fewest possible coins and print coins used
'''

def makeChange(coinlist, change, mincoins, coinused):
    '''
    coinsUsed - list of the coins used to make change for the amount corresponding to the position in the list
    coinCount -  minimum number of coins used to make change for the amount corresponding to the position in the list
    '''

    for value in range(change + 1):
        possible_coins = [i for i in coinlist if i <= value]
        minCount = value  #assume using coins of denomination 1 
        newCoin = 1       #assume using coins of denomination 1

        for coin in possible_coins:
            neededCoins = mincoins[value - coin] + 1
     	    if neededCoins < minCount:
                minCount = neededCoins
                newCoin = coin  


        mincoins.insert(value, minCount)
        coinused.insert(value, newCoin)

    return (mincoins[change], coinused)


def printCoins(amt, coinused):
    while amt > 0:
        coin = coinused[amt]
        print coin
        amt -= coin


def main():
    amnt = 149
    clist = [1,5,10,21,25]
   
    res, coinused = makeChange(clist, amnt, [], [])

    print 'Making change for amt {} needs {} coins'.format(amnt, res)
    print 'Coins used are:'
    printCoins(amnt, coinused)

if __name__ == '__main__':
    main()
                  	
