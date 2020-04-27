"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""366. Find Leaves of Binary Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    def findLeaves(self, root):
        result = []
        self.dfs(root, result)
        root = None
        return result  

    def dfs(self, root, result):
        if not root:
            return -1
        left_height = self.dfs(root.left, result)
        right_height = self.dfs(root.right, result)
        curr_height = 1 + max(left_height, right_height)
        if curr_height == len(result):
            result.append([])
        result[curr_height].append(root.val)
        root.left = root.right = None
        return curr_height