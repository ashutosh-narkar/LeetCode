#!/usr/bin/env python
"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""


# Solution 1: Same logic as anagram_3.py
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    if len(s1) > len(s2):
        return False

    charCount = {}
    for char in s1:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    count = len(s1)

    left, right = 0, 0

    while right < len(s2):
        if s2[right] in charCount:
            charCount[s2[right]] -= 1
            if charCount[s2[right]] >= 0:
                count -= 1

        if count == 0:
            return True

        if right - left + 1 == len(s1):
            if s2[left] in charCount:
                if charCount[s2[left]] >= 0:
                    count += 1

                charCount[s2[left]] += 1

            left += 1

        right += 1

    return False





# Solution 2:

# 1) How do we know string p is a permutation of string s?
# Easy, each character in p is in s too.
# So we can abstract all permutation strings of s to a map (Character -> Count). i.e. abba -> {a:2, b:2}.
# Since there are only 26 lower case letters in this problem, we can just use an array to represent the map.

# 2) How do we know string s2 contains a permutation of s1? We just need to create a sliding window with length of s1,
# move from beginning to the end of s2. When a character moves in from right of the window,
# we subtract 1 to that character count from the map. When a character moves out from left of the window,
# we add 1 to that character count.
# So once we see all zeros in the map, meaning equal numbers of every characters between s1 and
# the substring in the sliding window, we know the answer is true.



def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    l1 = len(s1)
    l2 = len(s2)

    if l1 > l2:
        return False

    count = [0] * 26  # lower case characters

    # first window
    for i in range(l1):
        index1 = ord(s1[i]) - ord('a')
        index2 = ord(s2[i]) - ord('a')

        count[index1] += 1        # char count of the 1st string
        count[index2] -= 1        # char found in the 2nd string

    if allZero(count):
        return True

    # sliding window
    for i in range(l1, l2):
        index1 = ord(s2[i]) - ord('a')
        index2 = ord(s2[i - l1]) - ord('a')

        count[index1] -= 1        # char entering the window
        count[index2] += 1        # char leaving the window

        if allZero(count):
            return True

    return False


def allZero(items):
    for item in items:
        if item != 0:
            return False

    return True