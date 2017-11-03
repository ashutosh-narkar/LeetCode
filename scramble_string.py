#!/usr/bin/env python
'''

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

eg. "rgeat" is a scrambled string of "great".
    "rgtae" is a scrambled string of "great".

Solution1: Recursion

The main idea is:

1) separate s1 into two parts, namely --s11--, --------s12--------
2) separate s2 into two parts, namely --s21--, --------s22--------, and test the corresponding part (s11 and s21 && s12 and s22) with isScramble.
3) separate s2 into two parts, namely --------s23--------, --s24--, and test the corresponding part (s11 and s24 && s12 and s23) with isScramble.
4) Note that before testing each sub-part with isScramble, anagram is used first to test if the corresponding parts are anagrams. If not, skip directly.
(for one string to be a scramble of the other, they should have the same characters ie. anagrams)

Runtime:
There are O(n) possible split points. At each point, there are two possibilities: with swap and without swap. 
At each point, we recursively check the two substrings until both of them are single character, which takes time O(2^k+2^(n-k)), 
where k and n-k are the lengths of the two substrings. So, this algorithm runs in exponential time, O(2^n), and space complexity is also exponential (recursion stack).


'''

def isScramble(self, s1, s2):

    if not s1 or not s2:
        return False

    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False


    if s1 == s2:
        return True


    for i in range(1, len(s1)):
        if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
            self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):             # very cool slicing
                return True

    return False


##########################################################################################################################
# DP - O(n^4)

def isScramble(s1, s2):

    # both empty
    if not (s1 or s2):
        return True

    # one of them empty
    if not s1 or not s2:
        return False

    # lengths unequal
    if len(s1) != len(s2):
        return False

    # equal
    if s1 == s2:
        return True

    n = len(s1)

   
    # a table of matches  
    # dp[i][j][k] = true iff s2.substring(j,j+k) is a scambled string of s1.substring(i,i+k)       
    dp = [[[False] * (n + 1) for j in range(n)]  for i in range(n)]


    for i in range(n):
        for j in range(n):
            dp[i][j][1] = s1[i] == s2[j]


    # length of substring for examination
    for k in range(1, n + 1):
        # loop through starting pos of s1
        for i in range(n - k + 1):
            # loop through starting pos of s2
            for j in range(n - k + 1):

                # p: split into [0..p] and [p+1..k]
                for p in range(1, k):

                    # left of s1 and left of s2
                    # right of s1 and right of s2
                    dp[i][j][k] |= dp[i][j][p] and dp[i + p][j + p][k - p]


                    # left of s1 and right of s2
                    # right of s1 and left of s2
                    dp[i][j][k] |= dp[i][j + k - p][p] and dp[i + p][j][k - p]
                

    return dp[0][0][-1]

