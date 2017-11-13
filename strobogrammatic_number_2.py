#!/usr/bin/env python
"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return  ["11","69","88","96"].
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
    print is_strobogrammatic(4)