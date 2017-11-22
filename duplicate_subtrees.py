#!/usr/bin/env python
"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees,
you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.


Solution: Similar to serialization logic + Traversal
"""


def find_duplicate_subtrees(root):
    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """
    if not root:
        return []

    nodes = dict()  # <some_path_pattern>: <list_of_root_nodes_with_that_pattern>
    helper(root, nodes)

    result = []

    for val in nodes.values():
        if len(val) > 1:
            result.append(val[0])

    return result


def helper(root, nodes):
    if not root:
        return '#'

    struct = str(root.val) + ',' + helper(root.left, nodes) + ',' + helper(root.right, nodes)
    if struct in nodes:
        nodes[struct].append(root)
    else:
        nodes[struct] = [root]

    return struct
