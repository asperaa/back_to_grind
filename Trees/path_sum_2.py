"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""113. Path Sum II [Slow Way]
"""
from collections import deque

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
        if not root.left and not root.right:
            curr_sum += root.val
            path.append(root.val)
            if curr_sum == summ:
                new_path = tuple(path)
                self.paths.append(list(new_path))
                path.pop()
                return
            path.pop()
            return
        path.append(root.val)
        self.path_sum_dfs(root.left, curr_sum+root.val, path, summ)
        self.path_sum_dfs(root.right, curr_sum+root.val, path, summ)
        if path:
            path.pop()
    
    def pathSum(self, root, summ):
        path = deque()
        self.path_sum_dfs(root, 0, path, summ)
        return self.paths

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    root.right.right.left = TreeNode(5)
    root.right.left = TreeNode(13)
    s = Solution()
    print(s.pathSum(root,22))