#!/usr/bin/env python
"""
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:

Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'

Runtime: O(N + alpha), N = number of given words, aplha =  number of characters in given alphabet
"""

from collections import deque


def alien_order(words):
    if not words:
        return ""

    result = ""
    graph = dict()   # character -> list of characters connected to the key
    degree = dict()  # in-degree of a character

    # initialize the in-degree of every character to 0
    for word in words:
        for ch in word:
            degree[ch] = 0

    # compare 2 words. Create an edge from the mismatching char of the first word to that of the second
    for i in range(len(words) - 1):
        curr = words[i]
        next = words[i + 1]

        min_length = min(len(curr), len(next))
        for j in range(min_length):
            if curr[j] != next[j]:
                val = graph.get(curr[j], set())

                if next[j] not in val:
                    val.add(next[j])
                    graph[curr[j]] = val

                    # update the in-degree
                    degree[next[j]] = degree[next[j]] + 1

                break


    # bfs on the graph
    q = deque()
    for key, val in degree.items():
        if val == 0:
            q.append(key)

    while q:
        ch = q.popleft()

        result += ch

        if ch in graph:
            for neigh in graph[ch]:
                degree[neigh] = degree[neigh] - 1
                if degree[neigh] == 0:
                    q.append(neigh)

    if len(result) == len(degree):
        return result

    return ""

if __name__ == '__main__':
    print alien_order(["caa", "aaa", "aab"])

    print alien_order(["baa", "abcd", "abca", "cab", "cad"])

    print alien_order(["wrt", "wrf", "er", "ett", "rftt"])
