# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class binaryTree:
    def __init__(self) -> None:
        self.root = None
    def setNode(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        
    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)


class Solution:
    def allPossibleFBT(self, n: int) -> list[binaryTree[TreeNode]]:
        