"""We are the captains of our ships, and we stay 'till the end. Wee see our stories through.
"""

"""501. Find Mode in Binary Search Tree [T - O(n) and S - O(n)]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, root, node_freq):
        if not root:
            return None
        node_freq[root.val] = node_freq.get(root.val, 0) + 1    
        self.mode_num = max(self.mode_num, node_freq[root.val])
        self.dfs(root.left)
        self.dfs(root.right)
    
    def findMode(self, root):
        if not root:
            return 0
        node_freq = {}
        self.mode_num = float('-inf')
        self.dfs(root, node_freq)
        ans = [key for key, value in node_freq.items() if value == self.mode_num]
        return ans