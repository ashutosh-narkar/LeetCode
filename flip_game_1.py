#!/usr/bin/env python
"""
You are playing the following Flip Game with your friend:
Given a string that contains only these two characters: + and -, you and your friend take turns to flip
two consecutive "++" into "--".
The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:
[
  "--++",
  "+--+",
  "++--"
]


If there is no valid move, return an empty list [].
"""


def flip_game(s):
    if not s:
        return []

    result = []

    for i in range(len(s) - 1):
        if s[i] == '+' and s[i + 1] == '+':
            s1 = s[: i]                        # the substring from beginning to before the current
            s2 = '--'                          # replace current and next index
            s3 = s[i + 2:]                     # the substring from after the next index to the end

            temp = s1 + s2 + s3
            result.append(temp)

    return result

if __name__ == '__main__':
    print flip_game('++++')
    print flip_game('+--+')