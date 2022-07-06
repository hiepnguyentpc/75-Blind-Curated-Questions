class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertBinaryTree(root):

    def invert(root):
        if root == None:
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        invert(root.left)
        invert(root.right)

    invert(root)
    return root