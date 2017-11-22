#!/usr/bin/env python
"""
Given a string containing of '0', '1' and '?' wildcard characters, generate all binary strings
that can be formed by replacing each wildcard character by '0' or '1'.

Input str = "1??0?101"
Output:
        10000101
        10001101
        10100101
        10101101
        11000101
        11001101
        11100101
        11101101

Solution: We pass index of next character to the recursive function.
If the current character is a wildcard character '?', we replace it by '0' or '1' and recurse for remaining characters.
"""


def generate_binary_strings(s):
    if not s:
        return []

    result = []
    helper(result, s, 0)
    return result


def helper(result, s, index):

    if index == len(s):
        result.append(s)
        return

    if s[index] == '?':
        s = s[: index] + '0' + s[index + 1:]
        helper(result, s, index + 1)

        s = s[: index] + '1' + s[index + 1:]
        helper(result, s, index + 1)

    else:
        helper(result, s, index + 1)

if __name__ == '__main__':
    s = '1??0?101'
    print generate_binary_strings(s)