#!/usr/bin/env python
"""
Given a non-negative integer num represented as a string, remove k digits from the number
so that the new number is the smallest possible.

Note:
1) The length of num is less than 10002 and will be >= k.
2) The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.


Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.


Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Solution: Go through the digits from left to right, remove previous digits if that makes the number smaller
(and if we still have to remove digits)
"""


def remove_k_digits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if not num:
        return 0

    result = []

    for d in num:
        while k > 0 and result and result[-1] > d:
            result.pop()
            k -= 1

        result.append(d)

    return ''.join(result[:-k or None]).lstrip('0') or '0'     # SOMETHING NEW
