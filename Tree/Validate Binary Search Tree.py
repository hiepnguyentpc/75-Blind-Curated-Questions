# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        mini = -math.inf
        maxi = math.inf

        def isBST(root, mini, maxi):
            if root is None:
                return True

            if root.val <= mini or root.val >= maxi:
                return False
            return isBST(root.left, mini, root.val) and isBST(root.right, root.val, maxi)

        return isBST(root, mini, maxi)

