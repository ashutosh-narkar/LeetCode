#!/usr/bin/env python
'''
Write a function to find the longest common prefix string amongst an array of strings.

Scan from the first character, if it is same for all the strings, go to the next character. 
Return the string until meet the different character.

The termination conditions are: 
(1) one string ends, then the longest prefix is the string itself. 
(2) The chars of same index are not the same, the longest prefix is the sub string from 0 to current index-1.


'''
def longestCommonPrefix(strs):

    if not strs:
        return ''

    if len(strs) == 1:
        return strs[0]


    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]

if __name__ == '__main__':
    data = ['foo', 'foog', 'food']
    print 'Longest common prefix for {} is {}'.format(data, longestCommonPrefix(data))
