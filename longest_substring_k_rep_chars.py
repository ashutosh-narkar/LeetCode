#!/usr/bin/env python
'''
Find the length of the longest substring T of a given string (consists of lowercase letters only)
such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

# Solution: For each h, apply Two Pointer Technique to find the longest substring with at least K repeating characters
# and the number of unique characters in substring is h.


# Why do we have the loop from 1 to 26 ?
# To apply two-pointer technique, we need to put some constraint on the sub-string within the window,
# i.e. the number of unique characters within the window.
# To this end, we can apply two-pointer technique on it but we also need another
# outer loop to explore every possible case, i.e. the number of unique characters within the window.
# If we get rid of the outer loop (h = 1 : 26), then we have no idea how many unique characters within the window.

def longestSubstring(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if not s:
        return 0

    d = 0

    for h in range(1, 27):
        charCount = [0] * 26
        begin = 0
        end = 0

        unique = 0
        noLessThanK = 0

        while end < len(s):

            if unique <= h:
                idx = ord(s[end]) - ord('a')
                if charCount[idx] == 0:
                    unique += 1
                charCount[idx] += 1

                if charCount[idx] == k:
                    noLessThanK += 1

                end += 1

            else:
                idx = ord(s[begin]) - ord('a')
                if charCount[idx] == k:
                    noLessThanK -= 1

                charCount[idx] -= 1

                if charCount[idx] == 0:
                    unique -= 1

                begin += 1

            if unique == h and unique == noLessThanK:
                d = max(d, end - begin)

    return d