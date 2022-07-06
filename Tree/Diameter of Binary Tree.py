# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        diameter = 0

        def longestPath(node):
            if node == None:
                return 0
            leftPath = longestPath(node.left)
            rightPath = longestPath(node.right)

            nonlocal diameter
            diameter = max(diameter, leftPath + rightPath)
            return max(leftPath, rightPath) + 1

        longestPath(root)
        return diameter
