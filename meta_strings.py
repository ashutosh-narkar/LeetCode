#!/usr/bin/env python
"""
Given two strings, the task is to check whether these strings are meta strings or not.
Meta strings are the strings which can be made equal by exactly one swap in any of the strings.
Equal string are not considered here as Meta strings.

Examples:
Input : str1 = "geeks"
        str2 = "keegs"
Output : Yes
By just swapping 'k' and 'g' in any of string,
both will become same.

Input : str1 = "rsting"
        str2 = "string
Output : No

Input :  str1 = "Converse"
         str2 = "Conserve"
Output : Yes
By just swapping 'v' and 's' in any of string,
both will become same.

Solution:
1. Check if both strings are of equal length or not, if not return false.

2. Otherwise, start comparing both strings and count number of unmatched characters
   and also store the index of unmatched characters.

3. If unmatched characters are more than 2 then return false.

4. Otherwise check if on swapping any of these two characters in any string would make the string equal or not.

5. If yes then return true. Otherwise return false.
"""


def are_meta_strings(s1, s2):
    if len(s1) != len(s2):
        return False

    unmatched = 0

    # To store indexes of previously mismatched
    # characters
    prev = -1
    curr = -1

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            unmatched += 1

            if unmatched > 2:
                return False

            # Store both unmatched characters of
            # both strings
            prev = curr
            curr = i

    if unmatched == 2 and s1[prev] == s2[curr] and s1[curr] == s2[prev]:
        return True

    return False

if __name__ == '__main__':
    assert are_meta_strings('geeks', 'keegs') == True

    assert are_meta_strings('rsting', 'string') == False

    assert are_meta_strings('Converse', 'Conserve') == True

    assert are_meta_strings('leetcode', 'leetcode') == False

    print 'Tests Passed'
