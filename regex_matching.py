#/usr/bin/env python
"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true

"""


def is_match(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    # dp[i][j] means the match status between s[:i] and p[:j], i.e.
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Update the corner case of matching two empty strings
    dp[0][0] = True

    # Update the corner case of when s is an empty string but p is not.
    # Since each '*' can eliminate the charter before it, the table is
    # horizontally updated by the one before previous
    for i in range(2, len(p) + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):

            #  Update the table by referring the diagonal element
            if p[j - 1] != '*':
                dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

            else:
                # Eliminations
                # Either refer to the one before previous or count the previous
                dp[i][j] = dp[i][j - 2] or dp[i][j - 1]

                # Propagations
                # If p's previous one is equal to the current s, with
                # helps of *, the status can be propagated
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] |= dp[i - 1][j]

    return dp[-1][-1]
