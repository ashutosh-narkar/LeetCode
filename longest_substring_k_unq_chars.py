#!/usr/bin/env python
"""
Find the longest substring with k unique characters in a given string

Given a string you need to print longest possible substring that has exactly M unique characters.
If there are more than one substring of longest possible length, then print any one of them.

Examples:

"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message.
"""

# Solution: Two Pointer Technique. Runtime: O(n)
# Idea is to maintain a window and add elements to the window till it contains unique elements less or equal k
# If unique elements exceed the required window size ie. 'k', start removing the elements from left side.

# This solution is similar to anagram_3.py and min_window_substring.py

def k_uniques(s, k):
    if not s:
        return ""

    if len(s) < k:
        return ""

    maxLen = 0
    result = ""

    left, right = 0, 0
    unique = 0

    charCount = {}

    while right < len(s):
        if s[right] not in charCount:
            charCount[s[right]] = 1          # unique character
            unique += 1
        else:
            charCount[s[right]] += 1

        while unique > k:
            if s[left] in charCount:
                charCount[s[left]] -= 1

                if charCount[s[left]] == 0:
                    unique -= 1

            left += 1

        # update result
        if right - left + 1 > maxLen:
            maxLen = right - left + 1
            result = s[left: right + 1]

        right += 1

    return result


if __name__ == '__main__':
   print k_uniques("aabbcc", 1)
   print k_uniques("aabbcc", 2)
   print k_uniques("aabbcc", 3)
   print k_uniques("aaabbb", 3)
   print k_uniques("abcbbbbcccbdddadacb", 2)