#!/usr/bin/env python
'''
Given a binary tree, print it vertically. The following example illustrates vertical order traversal.

          1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9 
               
              
The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

Solution:
We need to check the Horizontal Distances from root for all nodes. If two nodes have the same Horizontal Distance (HD),
then they are on same vertical line.

HD for root is 0, a right edge (edge connecting to right subtree) is considered as +1 horizontal distance 
and a left edge is considered as -1 horizontal distance.

For example, in the above tree, HD for Node 4 is at -2, HD for Node 2 is -1, HD for 5 and 6 is 0 and HD for node 7 is +2.
'''
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



'''
Iterative Solution: Modified level-order traversal

Runtime: O(nLogn)
'''
def verticalOrderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if not root:
        return []

    queue = deque()
    queue.append((root, 0))  # (node, HD). Root has HD = 0

    output = {}  # key is HD, val is list of nodes with that HD

    while queue:
        node, hd = queue.popleft()

        if hd not in output:
            output[hd] = [node.val]

        else:
            output[hd].append(node.val)

        if node.left:
            queue.append((node.left, hd - 1))

        if node.right:
            queue.append((node.right, hd + 1))


    # sort keys based on ascending order of HD
    sortedKeys = sorted(output.items(), key=lambda x: x[0])

    verticalOrder = []

    for hd, nodes in sortedKeys:
        verticalOrder.append(nodes)

    return verticalOrder


'''
Recursive Solution:

We can do preorder traversal of the given Binary Tree. 
While traversing the tree, we can recursively calculate HDs. We initially pass the horizontal distance as 0 for root. 

For left subtree, we pass the Horizontal Distance as Horizontal distance of root minus 1. 
For right subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1. 

For every HD value, we maintain a list of nodes in a hash map.
Whenever we see a node in traversal, we go to the hash map entry and add the node to the hash map using HD as a key in map.
'''


def verticalOrderTraversal_rec(root, result, hd):
        if not root:
            return

        if hd not in result:
            result[hd] = [root.val]
        else:
            result[hd].append(root.val)

        verticalOrderTraversal_rec(root.left, result, hd - 1)
        verticalOrderTraversal_rec(root.right, result, hd + 1)


def helper(root):
    if not root:
        return

    result = {}
    verticalOrderTraversal_rec(root, result, 0)

    # sort to print from lower to higher horizontal distance
    result = sorted(result.items(), key=lambda x: x[0])
    for k, v in result:
        print v





if __name__ == '__main__':
    root = TreeNode(1)
    left = root.left = TreeNode(2)
    right = root.right = TreeNode(3)

    left.left = TreeNode(4)
    left.right = TreeNode(5)

    right.left = TreeNode(6)
    right.right = TreeNode(7)


    right.left.right = TreeNode(8) 
    right.right.right = TreeNode(9)

    helper(root)

    print "\n"

    print verticalOrderTraversal(root)








