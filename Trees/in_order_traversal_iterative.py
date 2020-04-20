"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""94. Binary Tree Inorder Traversal [Iterative]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:

    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res