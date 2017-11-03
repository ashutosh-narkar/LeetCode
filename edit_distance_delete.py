#!/usr/bin/env python
'''
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

Solution: Very similar to edit_distance.py
'''


def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1)
    n = len(word2)

    # if word1 empty, ed = len(word2)
    if m == 0:
        return n

    # if word2 empty, ed = len(word1)
    if n == 0:
        return m

    # initialize to all 0s
    # a[i][j] stands for distance of first i chars of word1 and first j chars of word2
    a = [[0] * (n + 1) for i in range(m + 1)]

    # if we consider 0 characters of word1, ed = i characters of word2
    for i in range(n + 1):
        a[0][i] = i

    # if we consider 0 characters of word2, ed = i characters of word1
    for i in range(m + 1):
        a[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # match in last position
            if word1[i - 1] == word2[j - 1]:
                a[i][j] = a[i - 1][j - 1]

            # Since we're permitted to operate only one character at a time
            else:
                a[i][j] = min(a[i - 1][j], a[i][j - 1]) + 1  # here 1 is cost of matching char with '-'

    return a[-1][-1]