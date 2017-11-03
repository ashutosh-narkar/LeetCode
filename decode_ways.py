#!/usr/bin/env python
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

# Solution 1


def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """

    if not s:
        return 0

    # number of ways to decode a string of length provided by the index
    dp = [0] * (len(s) + 1)

    # dp[0] means an empty string will have one way to decode
    dp[0] = 1

    # dp[1] means the number of ways to decode a string of size 1
    # if the single character is between 1 and 9 (both included) there is one way to decode it
    dp[1] = 1 if s[0] >= '1' and s[0] <= '9' else 0

    # check one digit and two digit combinations
    for i in range(2, len(s) + 1):
        first = s[i - 1: i]
        second = s[i - 2: i]

        # single valid character has to be between 1 and 9 (both included)
        # Recurrence -> num(current) = num(current-1) + num(current-2)
        # eg. the number of ways of decoding a string of length 2 = # ways of decoding a string of length 1 (if valid) +
        #                                                           # ways of decoding a string of length 2 (if valid)
        if first >= '1' and first <= '9':
            dp[i] += dp[i - 1]

        # double valid character has to be between 10 and 26 (both included)
        if second >= "10" and second <= "26":
            dp[i] += dp[i - 2]

    return dp[len(s)]




# Solution 2
#Recurrence:
#res[i]= res[i-1] if s[i] is valid +  res[i-2] if s[i-1:i] is valid.

def numDecodings(s):
    if not s:
        return 0

    res = [0] * len(s)


    # check is s[0] is valid
    if s[0] != '0':
        res[0] = 1  # set res[0]

    if len(s) == 1:
        return res[0]

    # check s[1] is valid
    # for input '01' we get output '1' if we do not check s[0]. correct answer is '0'
    if s[0] != '0' and s[1] != '0':
        res[1] = 1

    # now check if s[0:2] is valid
    if isValid(s[:2]):
        res[1] += 1


    # DP
    for i in range(2, len(s)):
        # check if s[i] is valid
        if s[i] != '0':
            res[i] += res[i - 1]

        # check if substring from prev to current char is valid
        if isValid(s[i-1: i+1]):
            res[i] += res[i- 2]

    return res[-1]


def isValid(s):
    
    if not s:
        return False

    if s[0] == '0':
        return False

    if len(s) == 2:
        if s[0] > '2' or s[0] == '2' and s[1] > '6':
            return False

    return True

 
if __name__ == '__main__':
    data = '12'
    print 'The number of ways decoding {} is {}'.format(data, numDecodings(data))





















