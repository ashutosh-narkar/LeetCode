#!/usr/bin/env python
'''
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of
people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]   #  READ this from right to left
'''


def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    if not people:
        return []

    # first arrange people in order of increasing number of people ahead of them
    # this means the first person in the list has the least number of people ahead of him
    people = sorted(people, key=lambda x: x[1])

    # arrange them in decreasing order of height
    people = sorted(people, key=lambda x: -x[0])    # people = sorted(people, key=lambda x: x[0], reverse=True)

    result = []
    # use the number of people as the index in the result array
    for p in people:
        result.insert(p[1], p)

    return result
