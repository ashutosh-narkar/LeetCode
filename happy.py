#!/usr/bin/env python
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

'''
# Method 1

def isHappy(n):

    res = helper(n)
    visited = set()

    while res != 1 and res not in visited:
        visited.add(res)
        res = helper(res)

    return res == 1


def helper(n):

    result = 0

    while n > 0:
        last = n % 10
        result += (last ** 2)
        n /= 10

    return result

       
# Method 2: Think of the process as checking cycles in a linked list

def isHappy(n):

    if not n:
        return False

    a = n
    b = helper(n)

    # if 'a' becomes equal to 'b', we have a cycle and hence can't get a happy number
    while a != 1 and a != b:
        a = helper(a)
        b = helper(helper(b))

    return a == 1


# return sum of squares
def helper(n):

    result = 0

    while n > 0:
        last = n % 10
        result += (last ** 2)
        n /= 10

    return result

