#!/usr/bin/env python
"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

The weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level
integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

Solution:
Instead of multiplying by depth, add integers multiple times
(by going level by level and adding the unweighted sum to the weighted sum after each level)
"""


def depth_sum_reverse(nestedList):
    if not nestedList:
        return 0

    unweighted, weighted = 0, 0
    while nestedList:
        nextlevel = []
        for item in nestedList:
            if isinstance(item, list):
                nextlevel.extend(item)
            else:
                unweighted += item

        weighted += unweighted
        nestedList = nextlevel
    return weighted

if __name__ == "__main__":
    input = [[1,1],2,[1,1]]
    print depth_sum_reverse(input)

    input = [1,[4,[6]]]
    print depth_sum_reverse(input)