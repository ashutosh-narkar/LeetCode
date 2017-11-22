#!/usr/bin/env python
"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].


Solution: Maintain a BST and let each node keep track of the number of nodes in its left subtree

Runtime: O(nlogn)
Space: O(n)


Similar Problems Explanation:
https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs/2

Similar Problems:
count_of_range_sum.py
reverse_pairs.py
"""


def count_smaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    if not nums:
        return []

    count = [0] * len(nums)
    bst = BST()

    # Insert into BST and get left count.
    for i in range(len(nums) - 1, -1, -1):
        bst.insert(nums[i])
        count[i] = bst.query(nums[i])

    return count


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0  # number of nodes in left subtree


class BST:
    def __init__(self):
        self.root = None

    # Insert node into BST
    def insert(self, val):
        node = BSTNode(val)

        # no root
        if not self.root:
            self.root = node
            return

        current = self.root

        while current:
            # Insert left if smaller
            if node.val < current.val:
                current.count += 1  # Increase the number of left children
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    break

            # Insert right if larger or equal
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    break

    # Query the smaller count of the value
    def query(self, val):
        current = self.root
        count = 0

        while current:
            if val == current.val:
                return count + current.count

            elif val < current.val:
                current = current.left  # we need to find smaller values

            else:
                count += 1 + current.count  # val is also greater than all values
                # that are smaller than current's value
                current = current.right

        return 0
