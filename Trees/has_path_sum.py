"""we are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""112. Path Sum [Class Variable Use]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.is_path_sum = False
    
    def path_sum_helper(self, root, curr_sum, summ):
        if not root.left and not root.right:
            curr_sum += root.val
            if curr_sum == summ:
                self.is_path_sum = True
            return
        self.path_sum_helper(root.left, curr_sum+root.val, summ)
        self.path_sum_helper(root.right, curr_sum+root.val, summ)
    
    def hasPathSum(self, root, summ):
        self.path_sum_helper(root, 0, summ)
        return self.is_path_sum