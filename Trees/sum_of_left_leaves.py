"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""404. Sum of Left Leaves
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def sum_of_leaves_dfs(self, root, is_left_child):
        if not root:
            return None
        if not root.left and not root.right and is_left_child:
            self.summ += root.val
            return
        else:
            self.sum_of_leaves_dfs(root.left, True)
            self.sum_of_leaves_dfs(root.right, False)
    
    def sumOfLeftLeaves(self, root):
        self.summ = 0
        if not root:
            return self.summ
        self.sum_of_leaves_dfs(root, False)
        return self.summ
        