#!/usr/bin/env python
'''
Given a string S, find the longest palindromic substring in S.

Runtime: O(n^2)


Solution: This solution is almost same as the DP solution for palindromic_substrings.py

For O(n) solution look at Manacher's Algorithm.
'''

# Solution 1: Using DP
# dp(i, j) represents whether s(i ... j) can form a palindromic substring,
# dp(i, j) is true when s(i) equals to s(j) and s(i+1 ... j-1) is a palindromic substring.

# Why "j - i < 3" ? This means if we have only 3 chars in the substring, we need to check only the end chars ie s[i] == s[j]

def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    result = ""

    dp = [[False] * len(s) for i in range(len(s))]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True

            # update result
            if dp[i][j] and j - i + 1 > len(result):
                result = s[i: j + 1]  # j + 1 since the substring includes the char at index 'j'

    return result




# Solution 2 : Don't use

def longestPalindrome(s):
    if not s:
        return


    result1 = []
    result2 = []


    m, n = 0, len(s)

    while m < n:
        if not isPalindrome(s[m: n]):
            n -= 1
            continue
        result1.append(s[m:n])
        m = n
        n = len(s)

    m, n = 0, len(s)

    while m < n:
        if not isPalindrome(s[m: n]):
            m += 1
            continue
        result2.append(s[m:n])
        n = m
        m = 0

    
    # smaller the number of elements in the list, longer the palindrome
    result = result1 if len(result1) < len(result2) else result2

    longest_sub = ''

    for word in result:
        if len(word) > len(longest_sub):
            longest_sub = word

    return longest_sub


def isPalindrome(word):

    if not word:
	    return True
	
    m = 0
    n = len(word) - 1

    while(m < n):
        if word[m] != word[n]:
            return False

        m += 1
        n -= 1

    return True



if __name__ == '__main__':

    # Test Cases
    data = 'forgeeksskeegfor'
    res = longestPalindrome(data)
    assert res == 'geeksskeeg'


    data = 'abaaaaa'
    res = longestPalindrome(data)
    assert res == 'aaaa'

    data = 'aaabaaaa'
    res = longestPalindrome(data)
    assert res == 'aaabaaa'

    data = 'abaccddccefe'
    res = longestPalindrome(data)
    assert res == 'ccddcc'


    data = 'HYTBCABADEFGHABCDEDCBAGHTFYW1234567887654321ZWETYGDE'
    res = longestPalindrome(data)
    assert res == '1234567887654321'


    print 'Tests passed'


