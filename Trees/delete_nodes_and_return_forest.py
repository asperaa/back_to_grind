"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1110. Delete Nodes And Return Forest
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, root, forest):
        if not root:
            return None
        root.left = self.dfs(root.left, forest)
        root.right = self.dfs(root.right, forest)
        if root.val in self.to_delete_set:
            if root.left:
                forest.append(root.left)
            if root.right:
                forest.append(root.right)
            return None
        return root
    
    def delNodes(self, root, to_delete):
        self.to_delete_set = set(to_delete)
        forest = []
        if not root:
            return []
        if not root.val in self.to_delete_set:
            forest.append(root)
        self.dfs(root, forest)
        return forest
        
