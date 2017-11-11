#!/usr/bin/env python
'''
Write a program that takes an integer and prints out all ways to multiply smaller 
integers that equal the original number, without repeating sets of factors

PrintFactors(12)
12 * 1
6 * 2
4 * 3
3 * 2 * 2

*****
The largest possible prime factor of any integer n may be discovered by examining no more than sqrt(n) potential factors.
'''

import itertools
import sys

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def generate_factors(p):
    result = []
   
    for i in range(1, len(p)):
        perms = itertools.permutations(p,len(p))
        for perm in perms:
            val = reduce(lambda x, y: x * y, perm[i:])
            res = list(perm[:i])
            res.append(val)
            result.append(res)

    return result

if __name__ == '__main__':

    num = int(sys.argv[1])
    p =  primes(num)
    print 'print factorization of {} is {}'.format(num, p)
 
    unique = []
    for factor in  generate_factors(p):
        if factor not in unique:
            unique.append(factor)

    for factor in unique:
        print ' * '.join(map(str, factor))
