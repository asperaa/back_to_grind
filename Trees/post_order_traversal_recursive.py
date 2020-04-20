"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""145. Binary Tree Postorder Traversal [Recursive]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def post_order_traversal_helper(self, root, res):
        if root:
            self.post_order_traversal_helper(root.left, res)
            self.post_order_traversal_helper(root.right, res)
            res.append(root.val)
    
    def postorderTraversal(self, root):
        res = []
        self.post_order_traversal_helper(root, res)
        return res