class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p,q):
    if not q and not p:
        return True
    if not q or not p:
        return False
    if q.val != p.val:
        return False
    return isSameTree(p.right, q.right) and isSameTree(p.left,q.left)