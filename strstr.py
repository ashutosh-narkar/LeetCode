#!/usr/bin/env python
"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Good Explanation: https://www.topcoder.com/community/data-science/data-science-tutorials/introduction-to-string-searching-algorithms/

**** For explanation of how to create the KMP table look at shortest_palindrome.py ****
"""
# Solution 1: KMP algorithm


def str_str_kmp(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0

    if not haystack or len(needle) > len(haystack):
        return -1

    table = getKMPtable(needle)

    i = 0
    j = 0

    while i < len(haystack):

        # match
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        # pattern found
        if j == len(needle):
            return i - j

        # mismatch after j steps
        elif i < len(haystack) and haystack[i] != needle[j]:

            # move ahead in the string if we are at beginning of pattern. May be we find a match later
            if j == 0:
                i += 1

            # we do not need to match all characters since, we know pat[0 to j-1] matches txt[i-j to i-1]
            else:
                j = table[j - 1]

    return -1


def getKMPtable(s):
    # get lookup table
    table = [0] * len(s)

    index = 0

    for i in range(1, len(s)):
        if s[index] == s[i]:
            table[i] = table[i - 1] + 1
            index += 1

        else:
            index = table[i - 1]

            while index > 0 and s[index] != s[i]:
                index = table[index - 1]

            if s[index] == s[i]:
                index += 1

            table[i] = index

    return table


"""
Solution 2: Brute Force

The "naive" approach is easy to understand and implement but it can be too slow in some cases.
If the length of the text is n and the length of the pattern m,
in the worst case it may take as much as (n * m) iterations to complete the task.

It should be noted though, that for most practical purposes, which deal with texts based on human languages, 
this approach is much faster since the inner loop usually quickly finds a mismatch and breaks. 
A problem arises when we are faced with different kinds of "texts", such as the genetic code.
"""


# @param haystack, a string
# @param needle, a string
# @return an integer
def str_str_brute(haystack, needle):

    if not needle:
        return 0

    lh = len(haystack)
    ln = len(needle)

    if ln > lh:
        return -1

    # Iterate over 'lh-ln + 1' since it indicates the possible starting points
    # in the give text (or haystack) in which the pattern(or needle can be searched)
    # eg. text=ashutosh, pattern=ut, there are 7 possible position in the text where pattern can be searched from

    for i in range(lh - ln + 1):

        j = 0
        while haystack[i + j] == needle[j]:
            j += 1

            if j == ln:
                return i

    return -1
