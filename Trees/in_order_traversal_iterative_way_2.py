"""We are the captains of our ships and we stay 'till the end. We see our stories through. 
"""

"""94. Binary Tree Inorder Traversal
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

class Solution:

    def inorderTraversal(self, root):
        if not root:
            return []
        stack, order = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            order.append(node.val)
            root = node.right
        return order