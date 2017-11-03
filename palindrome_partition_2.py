#!/usr/bin/env python
'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return
[["aa","b"], ["a","a","b"]]
'''

# Don't use. Use DFS instead. There is a DP solution similar to Longest Palindromic Substring (O(n^2)) but cannot understand
# solution

import sys

def partition(s):

    result = []
    if not s:
        return result

    # only one character in string
    if len(s) == 1:
        return result.append([s])

    result1 = []

    m, n = 0, len(s)

    while (m < n):
        if not isPalindrome(s[m: n]):
            n -= 1
            continue

	    result1.append(s[m: n])
	    m = n
	    n = len(s)

    result.append(result1)

    if list(s) not in result:
	    result.append(list(s))

    return result

def isPalindrome(word):

    if not word:
	    return True

    m = 0
    n = len(word) - 1

    while (m < n):
	    if word[m] != word[n]:
	        return False

	    m += 1
	    n -= 1

    return True


##########################################################
# Using DFS. Runtime O(2 ^ n)
def partition(s):

    if not s:
        return []


    result = []
    dfs(s, result)
    return result


def dfs(s, result, temp=[]):

    if not s:
        result.append(list(temp))     # make copy of temp

    for i in range(1, len(s) + 1):
        if isPalindrome(s[:i]):
            temp.append(s[:i])
            dfs(s[i:], result, temp)
            temp.pop()


def isPalindrome(s):
    if not s:
        return True

    return s == s[::-1]








if __name__ == '__main__':
    data = sys.argv[1]

    res = partition(data)

    print 'Input {} . Palindromic partitions {}'.format(data, res)
