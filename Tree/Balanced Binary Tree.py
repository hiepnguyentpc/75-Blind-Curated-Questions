class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:
    def isBalanced(root):


        isBalance = True

        def calculateHeight(node):
            nonlocal isBalance
            if node == None:
                return 0
            leftHeight = calculateHeight(node.left)
            rightHeight = calculateHeight(node.right)
            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False
            return max(leftHeight, rightHeight) + 1

        return isBalance