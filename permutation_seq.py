#!/usr/bin/env python
'''
The set [1,2,3...n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

Runtime - O(n)

'''
from math import factorial

def getPermutation(n, k):

    nums = range(1, n + 1)
        
    # since the kth sequence is at index k - 1
    k -= 1

    res = ''

    for i in reversed(range(1, n + 1)):
 
        # calculate index of first digit of sequence
        index = k / factorial(i - 1)

        # add that digit to result and remove from list
        res += str(nums[index])
        nums.pop(index)

        # update k
        k %= factorial(i - 1)

    return res 

    


if __name__ == '__main__':
    n = 3
    k = 2
    print '{}th permutation sequence is {}'.format(k, getPermutation(n, k))








