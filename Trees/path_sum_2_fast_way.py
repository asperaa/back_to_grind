"""We are the captains of our ship, and we stay 'till the end. We see our stories through.
"""

"""113. Path Sum II [Fast Way]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.paths = []
    
    def path_sum_dfs(self, root, curr_sum, path, summ):
        if not root:
            return
        path.append(root.val)
        curr_sum += root.val
        if not root.left and not root.right and curr_sum == summ:
            self.paths.append(path[:])
        else:
            self.path_sum_dfs(root.left, curr_sum, path, summ)
            self.path_sum_dfs(root.right, curr_sum, path, summ)
        path.pop()
    
    def pathSum(self, root, summ):
        path = []
        self.path_sum_dfs(root, 0, path, summ)
        return self.paths
        
        