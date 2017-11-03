#!/usr/bin/env python
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Given "ab", "ca"; returns true
   we can map 'a' -> 'c', 'b' -> 'a'

'''
# Method1 - Runtime O(n^2)

def isIsomorphic(s, t):

    mappings = {}

    # unequal lengths
    if len(s) != len(t):
        return False


    for i, j in zip(s, t):

        if i in mappings:
            if mappings[i] != j:
                return False

        else:
            if j in mappings.values():
                return False

        mappings[i] = j

    return True


# Method2 - Use 2 arrays to store the mapped characters. Runtime O(n)

def isIsomorphic(s, t):

    # unequal lengths
    if len(s) != len(t):
        return False

    # since 256 ascii chars
    map = [None] * 256
    rmap = [None] * 256

    for i, j in zip(s, t):

        if map[ord(i)]:
            if map[ord(i)] != j:
                return False

        else:
            if rmap[ord(j)]:
                return False

        map[ord(i)] = j
        rmap[ord(j)] = i

    return True



