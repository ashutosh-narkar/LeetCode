#!/usr/bin/env python
'''
Fibonacci Series
'''
import sys

def fib_rec(n):
    if n <= 1:
        return n

    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_dp(n):
    if n <= 1:
        return n

    fib_table = [0] * (n + 1)
    fib_table[0] = 0
    fib_table[1] = 1
    fib_table[2] = 1
    for i in range(3, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table


def fib(n):
    a,b = 0,1
    for i in range(n):
        a, b = b,a+b
    return a

if __name__ == '__main__':

    print 'Iterative approach'
    for i in range(int(sys.argv[1])):
        print fib(i)

    print 'Recursive Approach'
    for i in range(int(sys.argv[1])):
        print fib_rec(i)

    print 'DP Approach'
    print fib_dp(i)
