#!/usr/bin/env python
"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "*") -> true
isMatch("aa", "a*") -> true
isMatch("ab", "?*") -> true
isMatch("aab", "c*a*b") -> false


Solution: Similar to regex_matching.py
"""


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    # dp[i][j] means the match status between s[:i] and p[:j], i.e.
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Update the corner case of matching two empty strings
    dp[0][0] = True

    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 1]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')

            else:
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[-1][-1]
