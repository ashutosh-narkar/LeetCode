#!/usr/bin/env python
"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.

Solution: Same as strobogrammatic_number_2.py
"""


def is_strobogrammatic(n):
    if n == 0:
        return [""]

    oddMidCandidate = ["0", "1", "8"]
    evenMidCandidate = ["11", "69", "88", "96", "00"]

    if n == 1:
        return oddMidCandidate

    if n == 2:
        return evenMidCandidate[:-1]

    if n % 2 == 1:
        pre, minCandidate = is_strobogrammatic(n - 1), oddMidCandidate

    else:
        pre, minCandidate = is_strobogrammatic(n - 2), evenMidCandidate

    positions = (n - 1) / 2

    result = []
    for item in pre:
        for c in minCandidate:
            num = item[: positions] + c + item[positions:]
            result.append(num)

    return result

if __name__ == '__main__':
    low, high = "50", "100"

    min_length = len(low)
    max_length = len(high)

    if min_length == max_length:
        result = is_strobogrammatic(min_length)
        for item in result:
            if low <= item <= high:
                print item

    else:
        result1 = is_strobogrammatic(min_length)
        result2 = is_strobogrammatic(max_length)
        result1.extend(result2)
        for item in result1:
            if low <= item <= high:
                print item
