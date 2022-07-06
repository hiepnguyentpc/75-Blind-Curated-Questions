class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def maxiumdepth(root):
    if root == None:
        return 0
    leftHeight = maxiumdepth(root.left)
    rightHeight = maxiumdepth(root.right)
    return max(leftHeight,rightHeight) + 1