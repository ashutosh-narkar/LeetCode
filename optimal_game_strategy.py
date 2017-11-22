#!/usr/bin/env python
"""
Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even.
We play a game against an opponent by alternating turns.

In each turn, a player selects either the first or last coin from the row, removes it from the row permanently,
and receives the value of the coin.

Determine the maximum possible amount of money we can definitely win if we move first.

Note: The opponent is as clever as the user.

OR

N pots, each with some number of gold coins, are arranged  in a line. You are playing a game against another player.
You take turns picking a pot of gold. You may pick a pot from either end of the line, remove the pot, and keep
the gold pieces. The player with the most gold at the end wins. Develop a strategy for playing this game.

Solution: DP
There are two choices:

1. The user chooses the ith coin with value Vi: The opponent either chooses (i+1)th coin or jth coin.
The opponent intends to choose the coin which leaves the user with minimum value.
i.e. The user can collect the value Vi + min(F(i+2, j), F(i+1, j-1))

2. The user chooses the jth coin with value Vj: The opponent either chooses ith coin or (j-1)th coin.
The opponent intends to choose the coin which leaves the user with minimum value.
i.e. The user can collect the value Vj + min(F(i+1, j-1), F(i, j-2) )
"""


def optimal_strategy_of_game(nums):
    if not nums:
        return 0

    n = len(nums)
    # maximum value that can be collected from i'th coin to j'th coin.
    dp = [[0] * n for _ in range(n)]

    for gap in range(n):
        i = 0
        for j in range(gap, n):
            # a = dp[i + 2][j]       if User chooses i and opponent chooses i + 1
            # b = dp[i + 1][j - 1]   if User chooses i and opponent chooses j or vice-versa
            # c = dp[i][j - 2]       if User chooses j and opponent chooses j - 1

            if i + 2 <= j:
                a = dp[i + 2][j]
            else:
                a = 0

            if i + 1 <= j - 1:
                b = dp[i + 1][j - 1]
            else:
                b = 0

            if i <= j - 2:
                c = dp[i][j - 2]
            else:
                c = 0

            dp[i][j] = max(nums[i] + min(a, b), nums[j] + min(b, c))

            i += 1

    return dp[0][n - 1]

if __name__ == '__main__':
    nums = [8, 15, 3, 7]
    assert optimal_strategy_of_game(nums) == 22

    nums = [2, 2, 2, 2]
    assert optimal_strategy_of_game(nums) == 4

    nums = [20, 30, 2, 2, 2, 10]
    assert optimal_strategy_of_game(nums) == 42

    nums = [6, 9, 1, 2, 16, 8]
    assert optimal_strategy_of_game(nums) == 23

    print 'Tests Passed'
