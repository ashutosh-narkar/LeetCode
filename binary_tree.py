#!/usr/bin/env python
'''
Binary Tree Class
'''

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def insertLeft(self, data):
        newNode = BinaryTree(data)
        if self.left:
            newNode.left = self.left
        self.left = newNode

    def insertRight(self, data):
        newNode = BinaryTree(data)
        if self.right:
            newNode.right = self.right
        self.right = newNode
