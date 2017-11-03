#!/usr/bin/env python
'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative 
positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Recurrence:
if the current character in S doesn't equal to current character T, 
then we have the same number of distinct subsequences as we had without the new character.

if the current character in S equal to the current character T, then the distinct number of subsequences: 
the number we had before plus the distinct number of subsequences we had with less longer T and less longer S.
'''

def numDistinct(S, T):

    m  = len(S)
    n = len(T)

    dp = [[0] * (n + 1) for i in range(m + 1)]

    # 1st row
    # if S is empty, number of distinct subseq = 0
    for i in range(n + 1):
        dp[0][i] = 0

    # 1st col:
    # if T is empty, number of distinct subseq = 1
    for i in range(m + 1):
        dp[i][0] = 1
        

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if S[i - 1] != T[j - 1]:
                dp[i][j] = dp[i - 1][j]

            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                

    return dp[-1][-1]

if __name__ == '__main__':

    s = 'rabbbit'
    t = 'rabbit'

    print 'Number of distince subsequences of {} in {} is {}'.format(t, s, numDistinct(s, t))     

    
    s = ''
    t = 'a'
    print 'Number of distince subsequences of {} in {} is {}'.format(t, s, numDistinct(s, t))  


   
