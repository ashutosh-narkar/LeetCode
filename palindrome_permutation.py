#!/usr/bin/env python
"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Solution: Maintain a char count
-- If the length is even. Each character should appear exactly times of 2, e.g. 2, 4, 6, etc..
-- If the length is odd. One and only one character could appear odd times.
"""

def can_permute_palindrome(s):
    if not s:
        return True

    char_count = dict()

    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    tolerance = 0
    for val in char_count.values():
        if val % 2 == 1:
            tolerance += 1

    if len(s) % 2 == 0:
        return tolerance == 0
    else:
        return tolerance == 1

if __name__ == '__main__':
    assert can_permute_palindrome("code") == False
    assert can_permute_palindrome("aab") == True
    assert can_permute_palindrome("carerac") == True
    assert can_permute_palindrome("aabcb") == True
    assert can_permute_palindrome("aabbcadad") == True
    assert can_permute_palindrome("abcd") == False

    print "Tests Passed"
