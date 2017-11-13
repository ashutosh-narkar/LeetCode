#!/usr/bin/env python
"""
Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings
in a group are shifted versions of each other. Two string S and T are called shifted if,

S.length = T.length
and
S[i] = T[i] + K for
1 <= i <= S.length  for a constant integer K

For example strings {acd, dfg, wyz, yab, mop} are shifted versions of each other.

Input  : str[] = {"acd", "dfg", "wyz", "yab", "mop",
                 "bdfh", "a", "x", "moqs"};

Output : a x
         acd dfg wyz yab mop
         bdfh moqs
All shifted strings are grouped together.

Solution:
The difference between consecutive characters for all character of string are equal.
As in above example take acd, dfg and mop

a c d -> 2 1
d f g -> 2 1
m o p -> 2 1


Since the differences are same, we can use this to identify strings that belong to same group.
The idea is to form a string of differences as key. If a string with same difference string is found,
then this string also belongs to same group.

For example, above three strings have same difference string, that is "21".

In below implementation, we add 'a' to every difference and store 21 as "ba".

"""


def group_shifted_string(words):
    if not words:
        return []

    diff_to_words = dict()

    for word in words:
        diff = ""
        for i in range(1, len(word)):
            val = ord(word[i]) - ord(word[i - 1])
            if val < 0:
                val = val + 26               # we add 26 because there are 26 lowercase letters

            diff += chr(val + ord('a'))      # we add ord('a') to normalize the difference

        if diff not in diff_to_words:
            diff_to_words[diff] = [word]
        else:
            diff_to_words[diff].append(word)

    return diff_to_words.values()

if __name__ == '__main__':
    print group_shifted_string(["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"])

    print group_shifted_string(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
