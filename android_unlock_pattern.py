#!/usr/bin/env python
"""
Given an Android  3x3  key lock screen and two integers  m  and  n , where 1 <= m <= n <= 9,
count the total number of unlock patterns of the Android lock screen,
which consist of minimum of  m  keys and maximum  n  keys.

Rules for a valid pattern:
1) Each pattern must connect at least  m  keys and at most  n  keys.

2) All the keys must be distinct.

3) If the line connecting two consecutive keys in the pattern passes through any other keys,
the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.

4)The order of keys used matters.

Solution: The general idea is DFS all the possible combinations from 1 to 9 and skip invalid moves along the way.
We can check invalid moves by using a jumping table. e.g. If a move requires a jump and the key that it is crossing
is not visited, then the move is invalid. Furthermore, we can utilize symmetry to reduce runtime


"""


def number_of_patterns(m, n):
    jump = [[0] * 10 for _ in range(10)]

    jump[1][3] = jump[3][1] = 2
    jump[4][6] = jump[6][4] = 5
    jump[7][9] = jump[9][7] = 8

    jump[1][7] = jump[7][1] = 4
    jump[2][8] = jump[8][2] = 5
    jump[3][9] = jump[9][3] = 6

    jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5

    count = 0

    visited = [False] * 10

    count += backtrack(1, 1, 0, m, n, visited, jump) * 4    # 1, 3, 7, 9 are symmetrical
    count += backtrack(2, 1, 0, m, n, visited, jump) * 4   # 2, 4, 6, 8 are symmetrical
    count += backtrack(5, 1, 0, m, n, visited, jump)

    return count


def backtrack(num, pattern_length, pattern_count, m, n, visited, table):
    if pattern_length >= m:   # only count if moves are atleast m
        pattern_count += 1

    if pattern_length > n:
        return pattern_count

    visited[num] = True
    for next in range(1, 10):
        jump = table[num][next]

        # If vis[i] is not visited and (two numbers are adjacent or skip number is already visited)
        if not visited[next] and (jump == 0 or visited[jump]):
            pattern_count = backtrack(next, pattern_length, pattern_count, m, n, visited, table)

    visited[num] = False
    return pattern_count

if __name__ == '__main__':
    print number_of_patterns(1, 1)
