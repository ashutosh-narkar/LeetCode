#!/usr/bin/env python
'''
There are n stairs, a person standing at the bottom wants to reach the top. 
The person can climb either 1 stair or 2 stairs at a time. 
Count the number of ways, the person can reach the top.

Sol:
The person can reach nth stair from either (n-1)th stair or from (n-2)th stair. 
Let the total number of ways to reach nth stair be 'ways(n)'. 
The value of 'ways(n)' can be written as following:
ways(n) = ways(n-1) + ways(n-2)

'''
import sys

def countways(n):
    result = fib(n)
    print 'Number of ways to reach {} steps is {}'.format(n, result)
   

def fib(n):
    fib_table = []
    fib_table.insert(0, 0)
    fib_table.insert(1, 1)
    fib_table.insert(2, 2)
    fib_table.insert(3, 3)

    for i in range (4, n + 1):
        val = fib_table[i - 1] + fib_table[i - 2] + fib_table[i - 3]
        fib_table.insert(i, val)

    return fib_table[-1]


if __name__  == '__main__':
    countways(int(sys.argv[1]))
