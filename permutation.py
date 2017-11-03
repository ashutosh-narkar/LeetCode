#!/usr/bin/env python
'''
Find all permutations of a string

Steps:
1) Remove the first letter
2) Find all the permutations of the remaining letters (recursive step)
3) Reinsert the letter that was removed in every possible location.

The base case for the recursion is a single letter. There is only one way to permute a single letter.

What if input is duplicated eg 'aba'. Return unique sol ???? TODO

'''
import sys

def permutations(word):
    if len(word) <= 1:
        return [word]   # since result is list of strings

    #get all permutations of length N-1
    perms=permutations(word[1:])
    char= word[0]

    result = []

    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result


if __name__ == '__main__':
   print permutations(sys.argv[1])
