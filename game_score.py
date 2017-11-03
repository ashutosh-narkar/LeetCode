#!/usr/bin/env python
'''
Count number of ways to reach a given score in a game

Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n,
find number of ways to reach the given score.

Examples:

Input: n = 20
Output: 4
There are following 4 ways to reach 20
(10, 10)
(5, 5, 10)
(5, 5, 5, 5)
(3, 3, 3, 3, 3, 5)

Input: n = 13
Output: 2
There are following 2 ways to reach 13
(3, 5, 5)
(3, 10)
'''

def count(n):

    # table[i] will store count of solutions for
    # value i
    table = [0] * (n + 1)

    # base case : If given value is 0
    table[0] = 1

    # One by one consider given 3 moves and update the table[]
    # values after the index greater than or equal to the
    # value of the picked move
    for i in range(3, n + 1):
        table[i] += table[i - 3]

    for i in range(5, n + 1):
        table[i] += table[i - 5]

    for i in range(10, n + 1):
        table[i] += table[i - 10]

    return table[n]

if __name__ == '__main__':

    print 'Number of ways to reach {} is {}'.format(20, count(20))
    print 'Number of ways to reach {} is {}'.format(13, count(13))
