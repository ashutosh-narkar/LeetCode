#!/usr/bin/env python
'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.


Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".




Solution: Use a sliding window approach.
Time Complexity will be O(n) because the "start" and "end" points will only move from left to right once.
'''


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    hash = {}  # hash stores the list of characters we need to cross-off. Initially has all of p in it
    for c in p:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1

    count = len(p)  # number of characters still to be crossed-off

    # initialize
    result = []
    left = 0
    right = 0

    while right < len(s):
        # for every iteration, check if current character is a desired char. if so, cross it off. otherwise, move on
        #  to the next character. Move right every time, if the character exists in p's hash, decrease the count
        #  current hash value >= 1 means the character is existing in p

        if s[right] in hash:
            hash[s[right]] -= 1

            if hash[s[right]] >= 0:
                count -= 1

        # when the count is down to 0, means we found the right anagram
        # then add window's left to result list
        if count == 0:
            result.append(left)

        # if we find the window's size equals to p, then we have to move left (narrow the window) to find the new match
        # window.
        # ++ to reset the hash because we kicked out the left
        # only increase the count if the character is in p
        # the count >= 0 indicate it was original in the hash, cuz it won't go below 0
        if right - left + 1 == len(p):
            if s[left] in hash:
                if hash[s[left]] >= 0:
                    count += 1
                hash[s[left]] += 1
            left += 1
        right += 1

    return result
