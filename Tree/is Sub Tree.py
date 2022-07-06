class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubTree(root, subRoot):


    def isIdentical(s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return isIdentical(s.right, t.right) and isIdentical(s.left, t.left)


    if root == None:
        return False
    if subRoot == None:
        return True

    if isIdentical(root, subRoot):
        return True

    return isSubTree(root.right, subRoot) or isSubTree(root.left, subRoot)
