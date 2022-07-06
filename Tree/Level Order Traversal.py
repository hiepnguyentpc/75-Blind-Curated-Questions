class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    levels = []

    def helper(node, level):
        if not node:
            return levels

        if level == len(levels):
            levels.append([])
        levels[level].append(node)
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
    helper(root, 0)
    return levels