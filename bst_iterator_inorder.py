#!/usr/bin/env python
'''
Inorder Traversal Iterator

OR


Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.


Average runtime of next() is O(1). Some cases make take O(n) or O(h). But average is O(1).
In the next(), if the smallest node does not have a right child, then runtime O(1).
If it has a right-child, we go its left-most node. This is O(n) for all nodes who have a right child.

And since we go through the entire tree, the average next() run time is O(n) / n = O(1)
'''

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.current = root

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack or self.current

    # @return an integer, the next smallest number
    def next(self):
        '''
        the smallest node is the leftmost node of the BST.
        then next smallest node, will be the smallest node's Right child
        '''

        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

        # smallest node
        node = self.stack.pop()
 
        # next smallest
        self.current = node.right
        return node.val

    

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
