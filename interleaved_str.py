#!/usr/bin/env python
"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = 'aabcc'
s2 = 'dbbca'

When s3 = 'aadbbcbcac', return true.
When s3 = 'aadbbbaccc', return false.

M = len(s1), N = len(s2)
Time Complexity: O(MN)
Auxiliary Space: O(MN)
"""


def is_interleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    if len(s3) != len(s1) + len(s2):
        return False

    # dp table represents if s3 is interleaving at (i+j)th position
    # when s1 is at ith position, and s2 is at jth position.
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # If both s1 and s2 are empty, s3 is empty too, and it is considered interleaving
    dp[0][0] = True

    # s1 is empty
    # Check if previous s2 position is interleaving and current
    # s2 position char is equal to s3 current position char,
    # it is considered interleaving
    for i in range(1, len(s2) + 1):
        dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

    # s2 is empty
    for i in range(1, len(s1) + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            val1 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]  # current char of s2 matches current char of s3
            val2 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]  # current char of s1 matches current char of s3
            dp[i][j] = val1 or val2

    return dp[len(s1)][len(s2)]    # dp[-1][-1]


if __name__ == '__main__':

    assert is_interleave("XXY", "XXZ", "XXZXXXY") == False
    assert is_interleave("XY" ,"WZ" ,"WZXY") == True
    assert is_interleave("XY", "X", "XXY") == True
    assert is_interleave("XXY", "XXZ", "XXXXZY") == True
    assert is_interleave("abcd", "xyz", "axybczd") == True
    assert is_interleave("AB", "CD", "CADB") == True
    assert is_interleave("AB" ,"CD" ,"CDAB") == True
    assert is_interleave("AB" , "A" , "AAB") == True
    assert is_interleave("A" ,"AB" ,"ABA") == True
    assert is_interleave("A" ,"AB", "BAA") == False
    assert is_interleave("ACA" ,"DAS" ,"DAACSA") == True
    assert is_interleave("ACA" ,"DAS" ,"DAASCA") == True
    assert is_interleave("A", "AB" ,"AAB") == True
    assert is_interleave("AAB" ,"AAC" ,"AACAAB") == True
    assert is_interleave("101", "01", "10011") == True
    assert is_interleave("101" ,"01" ,"11010") == False
    assert is_interleave("A" ,"C", "CA") == True
    assert is_interleave("A", "C", "CD") == False
    assert is_interleave("ACA" ,"DAS", "ADASAC") == False
    assert  is_interleave("YX", "X", "XXY") == False

    print 'Tests passed'










