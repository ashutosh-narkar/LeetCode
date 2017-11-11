#!/usr/bin/env python
"""
You are given two jugs with capacities x and y litres.
There is an infinite amount of water supply available.

You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1:

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False

Solution:
The basic idea is to use the property of Bezout's identity and check if z is a multiple of GCD(x, y)

Bezout's identity (also called Bezout's lemma) is a theorem in the elementary theory of numbers:

let a and b be nonzero integers and let d be their greatest common divisor. Then there exist integers x
and y such that ax+by=d

If a or b is negative this means we are emptying a jug of x or y gallons respectively.

Similarly if a or b is positive this means we are filling a jug of x or y gallons respectively.

For example, 4 = (-2) * 3 + 2 * 5, which means you pour in water twice with cup-5 and pour out water twice with cup-3.
Talk back to the question, it's like we first fill jug-5, pour water to jug-3 from jug-5, empty jug-3,
pour the remaining 2 water into jug-3 from jug-5, fill jug-5 again, pour water into jug-3 from jug-5,
empty jug-3, then we have only 4 water left in jug-5. It's exactly fill jug-5 twice and empty jug-3 twice.

"""


def canMeasureWater(x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    if x + y < z:
        return False

    # one of the jugs is empty
    if x == z or y == z or x + y == z:
        return True

    return z % gcd(x, y) == 0


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a
