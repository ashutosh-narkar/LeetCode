#!/usr/bin/env python
'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

def minDistance(word1, word2):

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
          
            # case 1 - match or mismatch in last position
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            val1 = a[i -1][j-1] + cost

            # case 2
            val2 = a[i -1][j] + 1     # here 1 is cost of matching char with '-'

            # case 3
            val3 = a[i][j - 1] + 1    # here 1 is cost of matching char with '-'

            a[i][j] = min(val1, val2, val3)

    return a[-1][-1]


