#!/usr/bin/env python
'''
Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

Example:
Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
import sys


def letterCombinations(digits):
    if not digits:
        return []

    letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    result = ['']   # empty string is needed otherwise letterCombinations("2") = [] instead of ["a","b","c"]

    for digit in digits:
        chars = letters[ord(digit) - 48]   # ord('0') = 48
        newresult = []

        for char in chars:
            for str in result:
                newresult.append(str + char)

        result = newresult

    return result


##################################################################
'''
Since there are no more than 4 possible characters for each digit, the number of
recursive calls T(n) satisfies T(n) ≤ 4T(n − 1), which solves to T(n) = O(4^n ). For the
function calls that entail recursion, the time spent within the function, not including
the recursive calls, is O(1). For the base case, printing a sequence of length n takes
time O(n). Therefore, the time complexity is O(4^n n).

'''


def letterCombinations_rec(digits):

    if not digits:
        return []

    mappings = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    result =[]
    combinations(digits, result, 0, mappings)
    return result

def combinations(digits, result, level, mappings, temp=[]):

    if level == len(digits):
        result.append(''.join(temp))
        return

    index = ord(digits[level]) - 48

    for i in range(len(mappings[index])):
        temp.append(mappings[index][i])
        combinations(digits, result, level + 1, mappings, temp)
        temp.pop()


if __name__ == '__main__':
    
    data = sys.argv[1]
    print 'All combinations of {} are {}'.format(data, letterCombinations(data))
