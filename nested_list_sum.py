#!/usr/bin/env python
"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)
"""

from collections import deque

# Iterative Solution: Similar to BFS
def depthSum(nums):
    if not nums:
        return 0

    queue = deque()
    for item in nums:
        queue.append((item, 1))    # Initial depth is 1

    result = 0
    while queue:
        item, depth = queue.popleft()

        if isinstance(item, list):
            for num in item:
                queue.append((num, depth + 1))
        else:
            result += depth * item

    return result


# Recursive Solution
def depthSum_rec(nums):
    if not nums:
        return 0

    return xsum(nums, 1)


def xsum(nums,level):
    res = 0
    if nums:
        for num in nums:
            if isinstance(num,list):
                res += xsum(num,level+1)
            else:
                res += num * level

    return res

if __name__ == "__main__":
    input = [[1,1], 2, [1,1]]
    print depthSum_rec(input)

    input = [1, [2, 3]]
    print depthSum_rec(input)

    input = [1, [2, [3]]]
    print depthSum_rec(input)
