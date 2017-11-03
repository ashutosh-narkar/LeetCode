#!/usr/bin/env python
'''
How to count number of ways if the person can climb up to m stairs for a given value m? 
For example if m is 4, the person can climb 1 stair or 2 stairs or 3 stairs or 4 stairs at a time.

We can write the recurrence as following.

ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... ways(n-m, m) 
'''
import sys

def countWays(n, m):
    '''
    n is number of stairs
    m is number of ways
    '''

    result = countUtil(n + 1, m)
    print '{} stairs can be climbed in {} ways in {} step sizes'.format(n, result, m)


def countUtil(n, m):
    fib_table = []
    fib_table.insert(0, 0)
    fib_table.insert(1,1)

    for i in range(2, n+1):
        fib_table.insert(i, 0)
        for j in range(1, m + 1):
            if j <= i:
                fib_table[i] += fib_table[i - j]
    return fib_table[-1]


if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    countWays(n , m)
