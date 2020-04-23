"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""437. Path Sum III
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def path_sum_dfs(self, root, target, curr_path_sum, cache):
        if not root:
            return
        curr_path_sum += root.val
        old_path_sum = curr_path_sum - target
        self.result += cache.get(old_path_sum, 0)
        cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1
        self.path_sum_dfs(root.left, target, curr_path_sum, cache)
        self.path_sum_dfs(root.right, target, curr_path_sum, cache)
        cache[curr_path_sum] -= 1
    
    def pathSum(self, root, target):
        self.result = 0
        cache = {0:1}
        self.path_sum_dfs(root, target, 0, cache)
        return self.result
