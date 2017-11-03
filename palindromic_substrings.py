#!/usr/bin/env python
'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.

Solution: This solution is almost same as the DP solution for longest_palindromic_substring.py,
instead of storing the longest, just get the count of palindromic substrings.
'''


def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return ""

    result = 0

    dp = [[False] * len(s) for i in range(len(s))]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
            if dp[i][j]:
                result += 1

    return result


# Alternate solution using "center expansion"
# https://discuss.leetcode.com/topic/96822/python-straightforward-with-explanation-bonus-o-n-solution