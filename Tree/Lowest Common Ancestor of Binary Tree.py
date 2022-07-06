class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):

    ans = None

    def recurseTree(curr):
        nonlocal ans
        if curr == None:
            return 0

        left = recurseTree(curr.left)
        right = recurseTree(curr.right)

        mid = False
        if curr == q or curr == q:
            mid = True

        if mid + left + right >= 2:
            ans = curr

        return mid or left or right

    recurseTree(root)
    return ans

def LCABruteForce(root, p, q):


    def findPath(root, node_needed, path):
        if not root:
            return False
        path.append(root)
        if root == node_needed:
            return True
        if (root.left and findPath(root.left, node_needed,path)) or (root.right and findPath(root.right, node_needed, path)):
            return True
        path.pop()
        return False
    path1 = []
    findPath(root, p, path1)
    path2 = []
    findPath(root, q, path2)
    i = 0
    while i < len(path1) and i < len(path2):
        #find the first different parent
        if path1[i] != path2[i]:
            break
        i+=1

    return path1[i-1]












"""

[TreeNode{val: 3, 
          left: 
              TreeNode{val: 5, 
                       left: 
                           TreeNode{val: 6, 
                                      left: None, right: None}, 
                        right: 
                            TreeNode{val: 2, 
                                    left: TreeNode{val: 7, left: None, right: None}, 
                                    right: TreeNode{val: 4, left: None, right: None}}}, 
        right: TreeNode{val: 1, 
                        left: TreeNode{val: 0, left: None, right: None}, 
                       right: TreeNode{val: 8, left: None, right: None}}}]
"""


