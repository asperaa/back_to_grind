"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""144. Binary Tree Preorder Traversal [Recursive]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def preorder_helper(self, root, res):
        if root:
            res.append(root.val)
            self.preorder_helper(root.left, res)
            self.preorder_helper(root.right, res)

    def preorderTraversal(self, root):
        res = []
        self.preorder_helper(root, res)
        return res
