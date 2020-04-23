"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""938. Range Sum of BST
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    def __init__(self):
        self.range_sum = 0
    
    def rangeSumBSTHelper(self, root, L, R):
        if not root:
            return
        if root.val >= L and root.val <= R:
            self.range_sum += root.val
        if root.val > L:
            self.rangeSumBSTHelper(root.left, L, R)
        if root.val < R: 
            self.rangeSumBSTHelper(root.right, L, R)
    
    def rangeSumBST(self, root, L, R):
        self.rangeSumBSTHelper(root, L, R)
        return self.range_sum        