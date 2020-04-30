"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""701. Insert into a Binary Search Tree [Iterative]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def insertIntoBST(self, root, val):
        if not root:
            return None
        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right