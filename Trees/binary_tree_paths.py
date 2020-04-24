"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""257. Binary Tree Paths
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, root, curr_path):
        if not root:
            return None
        new_node = str(root.val)
        if not root.left and not root.right:
            self.paths.append(curr_path + new_node)
        else:
            self.dfs(root.left, curr_path + new_node + "->")
            self.dfs(root.right, curr_path + new_node + "->")
    
    def binaryTreePaths(self, root):
        if not root:
            return []
        self.paths = []
        self.dfs(root, "")
        return self.paths  