#!/usr/bin/env python
'''
Count the number of prime numbers less than a non-negative number, n.

Solution: Sieve of Eratosthenes
For explanation see example at https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

'''

def count_primes(n):
    """
    :type n: int
    :rtype: int
    """
    # if n is 2 or lower, there are 0 primes
    if n <= 2:
        return 0
                                                                                
    # make a boolean array of each number 'including' n
    # For ex primes[0] = False, means '0' is not a prime number
    primes = [True] * (n + 1)
                                                                                                
    primes[0], primes[1] = False, False
                                                                                                                
    for i in range(2, n + 1):
        if primes[i]:
            j = 2           # since 'i' is a prime number, all multiples of 'i' are not prime
            while i * j <= n:
                primes[i * j] = False
                j += 1
    
    # Since we are counting primes less than the number itself, we dont include the index of the number
    # for ex if n = 4,
    # primes  = [False, False, True, True, False]
    return sum(primes[:-1])
