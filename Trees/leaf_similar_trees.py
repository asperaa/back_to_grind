"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""872. Leaf-Similar Trees [T - O(n1 + n2) and S - O(n1+n2)]
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, root, leaves):
        if not root:
            return
        self.dfs(root.left, leaves)
        self.dfs(root.right, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)

    def leafSimilar(self, t1, t2):
        leaves_1, leaves_2 = [], []
        self.dfs(t1, leaves_1)
        self.dfs(t2, leaves_2)
        return leaves_1 == leaves_2 

