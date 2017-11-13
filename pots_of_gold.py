#!/usr/bin/env python
"""
Pots of gold game: Two players A & B. There are pots of gold arranged in a line, each containing some gold coins
(the players can see how many coins are there in each gold pot - perfect information).
They get alternating turns in which the player can pick a pot from one of the ends of the line.
The winner is the player which has a higher number of coins at the end.
The objective is to "maximize" the number of coins collected by A, assuming B also plays optimally. A starts the game.

Solution:

The idea is to find an optimal strategy that makes player A win knowing that player B is playing optimally as well.
The player has 2 choices for the coin[i....j] where i and j represent front and rear of the line respectively.


CASE 1:
If player A chooses from pot i, player B is left to choose from [i+1 to j]
    1. If player B chooses from pot i + 1, recurse for [i + 2...j]
    2. If player B chooses from pot j, recurse for [i + 1...j - 1]

CASE 2:
If player B chooses from pot j, player B is left to choose from [i to j - 1]
    1. If player B chooses from pot i, recurse for [i + 1...j - 1]
    2. If player B chooses from pot j - 1, recurse for [i...j - 2]


Resources:
http://www.techiedelight.com/pots-gold-game-dynamic-programming/

Runtime: O(n^2)
Space Complexity: O(n^2)
"""


def pots_of_gold(coin):
    if not coin:
        return 0

    dp = [[0] * len(coin) for _ in range(len(coin))]
    return optimal_strategy(coin, 0, len(coin) - 1, dp)


def optimal_strategy(coin, i, j, dp):

    # base case: One pot left
    if i == j:
        return coin[i]

    # 2 pots left
    if i + 1 == j:
        return max(coin[i], coin[j])

    if dp[i][j] == 0:
        # CASE 1
        start = coin[i] + min(optimal_strategy(coin, i + 2, j, dp), optimal_strategy(coin, i + 1, j - 1, dp))

        # CASE 2
        end = coin[j] + min(optimal_strategy(coin, i + 1, j - 1, dp), optimal_strategy(coin, i, j - 2, dp))

        dp[i][j] = max(start, end)

    # return the subproblem solution
    return dp[i][j]

if __name__ == '__main__':
    coin = [4, 6, 2, 3]
    print pots_of_gold(coin)

    coin = [3, 9, 1, 2]
    print pots_of_gold(coin)