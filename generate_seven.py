#!/usr/bin/env python
"""
Given a function foo() that returns integers from 1 to 5 with equal probability,
write a function that returns integers from 1 to 7 with equal probability using foo() only.

Minimize the number of calls to foo() method. Also, use of any other library function is not allowed
and no floating point arithmetic allowed.

Solution:
We know foo() returns integers from 1 to 5. How we can ensure that integers from 1 to 7 occur with equal probability ?
If we somehow generate integers from 1 to a-multiple-of-7 (like 7, 14, 21,..) with equal probability,
we can use modulo division by 7 followed by adding 1 to get the numbers from 1 to 7 with equal probability.

1) We can generate numbers from 1 to 25 with equal probability using the following expression.
x = 5 foo() + foo() - 5
when foo() = 1, x = 1
when foo() = 5, x = 25

2) So if x generates a number less than 22, we return (x % 7 + 1)

3) If x generates a number more than or equal to 22, we recurse.

The probability of returning each integer thus becomes 1/7.
"""
import random


def foo():
    return random.randint(1, 5)


def rand_seven():

    x = 5 * foo() + foo() - 5

    if x < 22:
        return (x % 7) + 1

    return rand_seven()

if __name__ == '__main__':
    print rand_seven()
