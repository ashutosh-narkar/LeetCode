#!/usr/bin/env python
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

For example, given s = "aab"
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

Runtime: O(n^2)
'''
############################
# DP
# The time complexity and the space complexity are both O(n ^ 2).

def minCut(s):

    if not s:
        return 0


    n = len(s)

    table = [[False] * (n + 1) for i in range(n + 1)]    # table[i][j] = true means s[i:j] is a valid palindrome

    dp = [i - 1 for i in range(n + 1)]                    # dp[i] means the minCut for s[0:i] to be partitioned, initialized with max cuts ie. max cuts for s[:2] = 1

    for i in range(2, n + 1):
        # look at every char upto the beginning of 's'
        for j in range(i - 1, -1, -1):
            # chars shud be equal and everything betwwen them shud be a palindrome or there shud be only 1 char between them
            if s[i - 1] == s[j] and (table[j + 1][i - 1] or i - j - 1 < 2):
                table[j][i] = True
                dp[i] = min(dp[i], dp[j]  + 1)   # d[j] + 1 since that +1 represents a cut

                
    return dp[-1]


################################

import sys

def minCut(s):
    if not s:
        return -1

    # if only one character in string
    if len(s) == 1:
        return 0

    result1 = []
    result2 = []

    m, n = 0, len(s)

    while (m < n):
        if not isPalindrome(s[m: n]):
            n -= 1
            continue

        result1.append(s[m: n])
        m = n
        n = len(s)

  
    m, n = 0, len(s)
    while (m < n):
        if not isPalindrome(s[m: n]):
            m += 1
            continue

        result2.append(s[m: n])
        n = m
        m = 0

    result = min(len(result1), len(result2))

    return result - 1


def isPalindrome(word):
    if not word:
        return True

    m = 0
    n = len(word) - 1

    while (m < n):
        if word[m] != word[n]:
            return False

        m += 1
        n -= 1

    return True





if __name__ == '__main__':
    data = sys.argv[1]

    print 'Min Cuts needed for partitioning {} is {}'.format(data, minCut(data))
