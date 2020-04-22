"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""543. Diameter of Binary Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.dia = 0
    
    def dia_helper(self, root):
        if not root:
            return 0
        l_height = self.dia_helper(root.left)
        r_height = self.dia_helper(root.right)
        self.dia = max(self.dia, l_height+r_height)
        return 1 + max(l_height, r_height)

    def diameterOfBinaryTree(self, root):
        self.dia_helper(root)
        return self.dia
        