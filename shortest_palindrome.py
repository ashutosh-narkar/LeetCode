#!/usr/bin/env python
"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

Solution: KMP algorithm

Explanation: https://discuss.leetcode.com/topic/27261/clean-kmp-solution-with-super-detailed-explanation
Runtime: O(n)
"""


def shortest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    temp = s + "#" + s[::-1]
    table = getKMPtable(temp)

    # get the maximum palindrome part in s starts from 0

    # the value in the last entry of the 'table' array,
    # indicates the length of the longest palindromic substring starting from index 0 in the original string.
    # So we take all the characters that are after the palindromic substring and reverse them and add them
    # to the beginning of the original string. Thus the entire string now becomes a palindrome

    return s[table[-1]:][::-1] + s


def getKMPtable(s):
    # get lookup table
    table = [0] * len(s)

    # pointer that points to matched char in prefix part
    index = 0

    # skip index 0, we will not match a string with itself
    for i in range(1, len(s)):
        if s[index] == s[i]:
            # we can extend match in prefix and postfix
            table[i] = table[i - 1] + 1
            index += 1

        else:
            # match failed, we try to match a shorter substring

            # by assigning index to table[i-1], we will shorten the match string length,
            # and jump to the prefix part that we used to match postfix ended at i - 1

            index = table[i - 1]

            while index > 0 and s[index] != s[i]:
                index = table[index - 1]

            # if match, then extend one char
            if s[index] == s[i]:
                index += 1

            table[i] = index

    return table

if __name__ == '__main__':
    print shortest_palindrome('aacecaaa')
