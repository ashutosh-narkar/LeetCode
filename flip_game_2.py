#!/usr/bin/env python
"""
You are playing the following Flip Game with your friend:
Given a string that contains only these two characters: + and -, you and your friend take turns to flip
two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore
the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.
For example, given s = "++++", return true. The starting player can guarantee a win by flipping
the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.


Solution: Backtracking + Memoization
We can basically try every possible move for the first player and recursively check if the second player has
any chance to win. If the second player is guaranteed to lose, then we know the current move
the first player takes must be the winning move.


Runtime:
Suppose originally the board of size N contains only '+' signs, then roughly we have:

T(N) = (N-2) * T(N-2) = (N-2) * (N-4) * T(N-4) ... = (N-2) * (N-4) * (N-6) * ... ~ O(N!!)
"""


def can_win(s):
    if not s:
        return False

    moves = dict()   # input string > can win or not
    return can_win_helper(s, moves)


def can_win_helper(s, moves):
    if s in moves:
        return moves[s]

    for i in range(len(s) - 1):
        if s[i] == '+' and s[i + 1] == "+":
            s1 = s[:i]
            s2 = '--'
            s3 = s[i + 2:]
            s = s1 + s2 + s3

            other_player_wins = can_win_helper(s, moves)

            # reset
            s1 = s[:i]
            s2 = '++'
            s3 = s[i + 2:]
            s = s1 + s2 + s3

            if not other_player_wins:
                moves[s] = True
                return True

    moves[s] = False
    return False

if __name__ == '__main__':
    print can_win('++++')
    print can_win('++++++++')