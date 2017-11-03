#!/usr/bin/env python
'''
Preorder Traversal Iterator

For example, given a binary tree below,
   *       4
   *      / \
   *     2   6
   *    / \ / \
   *   1  3 5  7
   * the outputs will be 4, 2, 1, 3, 6, 5, 7. 
'''

# Definition for a  binary tree node

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        # add root as it need to be popped first
        self.stack.append(root)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.stack:
            return True

        return False


    # @return an integer, the next smallest number
    def next(self):
        '''
        Each time when we visit a node, we push its right and left children into the stack so 
        that we can access left subtree first and then right subtree.
        '''

        # retrieve element at stack top
        node = self.stack.pop()

        # add right node first  then left, as left will get popped first
        if node.right:
            self.stack.append(node.right)

        if node.left:
            self.stack.append(node.left)

        return node.val
            

if __name__ == '__main__':
 
    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(6)

    root.left  = left
    root.right = right

    left_left = TreeNode(1)
    left_right = TreeNode(3)
    left.left = left_left
    left.right = left_right


    right_left = TreeNode(5)
    right_right = TreeNode(7)
    right.left = right_left
    right.right = right_right  
 
    v = BSTIterator(root)
    result = [] 

    while v.hasNext(): 
        result.append(v.next())


    print result

