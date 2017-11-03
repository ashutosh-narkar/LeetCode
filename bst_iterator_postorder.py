#!/usr/bin/env python
'''
Postorder Traversal Iterator

For example, given a binary tree below,
   *       4
   *      / \
   *     2   6
   *    / \ / \
   *   1  3 5  7
   * the outputs will be 1 3 2 5 7 6 4. 
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
        self.current = root    
    

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.stack or self.current:
            return True

        return False


    # @return an integer, the next smallest number
    def next(self):
        '''
        Each time we pop out a node from the stack, we check whether it is the left child of the current top of the stack. 
        If so, repeat the step above on the right sub-tree of the current top. 
        '''

        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

        node = self.stack.pop()     

        # self.current should be current node's parent's right child
        if self.stack and node == self.stack[-1].left:
            self.current = self.stack[-1].right        

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

