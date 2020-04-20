"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""144. Binary Tree Preorder Traversal [Iterative]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def preorderTraversal(self, root):
        if not root:
            return []
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            root = node.right
        return res
