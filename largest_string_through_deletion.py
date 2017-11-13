#!/usr/bin/env python
"""
Giving a dictionary and a string 'str', find the longest string in dictionary which can be formed
by deleting some characters of the given 'str'.

Input : dict = {"ale", "apple", "monkey", "plea"}
        str = "abpcplea"
Output : apple

Input  : dict = {"pintu", "geeksfor", "geeksgeeks", " forgeek"}
         str = "geeksforgeeks"
Output : geeksgeeks


Solution:
We traverse all dictionary words and for every word, we check if it is subsequence of given string
and is largest of all such words. We finally return the longest word with given string as subsequence.

Runtime: O(N * n) , N = length of dict, n = length of target string


LeetCode question: Longest Word in Dictionary through Deleting
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting
some characters of the given string.
If there are more than one possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

**** For lexicographical order: words = sorted(words) ****

"""


def find_longest_string(words, target):

    result = ""
    max_length = 0

    for word in words:

        if is_subsequence(word, target) and len(word) > max_length:
            result = word
            max_length = len(word)

    return result


# Return true is str1 is a subsequence of str2
def is_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    i = 0
    j = 0
    while i < m and j < n:
        if str1[i] == str2[j]:
            i += 1
            j += 1

        else:
            j += 1

    return i == m

if __name__ == '__main__':
    words = ["ale", "apple", "monkey", "plea"]
    print find_longest_string(words, 'abpcplea')

    words = ["pintu", "geeksfor", "geeksgeeks", " forgeek"]
    print find_longest_string(words, 'geeksforgeeks')
