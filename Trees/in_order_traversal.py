"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""94. Binary Tree Inorder Traversal [Recursive]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    def in_order_helper(self, root, res):
        if root:
            self.in_order_helper(root.left, res)
            res.append(root.val)
            self.in_order_helper(root.right, res)

    def inorderTraversal(self, root):
        res = []
        self.in_order_helper(root, res)
        return res