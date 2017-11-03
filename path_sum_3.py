#!/usr/bin/env python
'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.


Example:

    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


Solution:
Each time find all the path start from current node
Then move start node to the child and repeat.
Time Complexity should be O(N^2) for the worst case and O(NlogN) for balanced binary Tree.

If the tree is balanced, then each node is reached from its ancestors (+ itself) only, which are up to log n.
Thus, the time complexity for a balanced tree is O (n * log n).

However, in the worst-case scenario where the binary tree has the same structure as a linked list, the time complexity is indeed O (n ^ 2).
'''


def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """

    if not root:
        return 0

    return findPath(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum)


def findPath(root, sum):
    res = 0

    if not root:
        return res

    if sum == root.val:
        res += 1

    res += findPath(root.left, sum - root.val)
    res += findPath(root.right, sum - root.val)
    return res

