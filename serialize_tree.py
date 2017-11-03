#!/usr/bin/env python
"""
Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection link
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string
and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.

Solution: Use level-order traversal
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = deque()
        queue.append(root)

        result = ''

        while queue:
            node = queue.popleft()

            if node:
                result += str(node.val) + ","
                queue.append(node.left)
                queue.append(node.right)

            else:
                result += "#,"

        # remove the last ','
        result = result[:-1]
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        data = data.split(',')

        root = TreeNode(int(data[0]))

        queue = deque()
        queue.append(root)

        i = 1
        while queue:
            node = queue.popleft()

            if not node:
                continue

            if data[i] != "#":
                node.left = TreeNode(int(data[i]))
            else:
                node.left = None

            queue.append(node.left)

            i += 1

            if data[i] != "#":
                node.right = TreeNode(int(data[i]))
            else:
                node.right = None

            queue.append(node.right)

            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))