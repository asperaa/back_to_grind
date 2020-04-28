"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1325. Delete Leaves With a Given Value
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, root):
        if not root:
            return True
        is_left_subtree_unival = self.dfs(root.left)
        is_right_subtree_unival = self.dfs(root.right)
        if not root.left and not root.right:
            self.unival_subtrees += 1
            return True
        elif is_left_subtree_unival and is_right_subtree_unival:
            if root.left and root.right and root.left.val == root.right.val and root.left.val == root.val:
                self.unival_subtrees += 1
                return True
            elif root.left and not root.right and root.left.val == root.val:
                self.unival_subtrees += 1
                return True
            elif root.right and not root.left and root.right.val == root.val:
                self.unival_subtrees += 1
                return True
        return False
    
    def countUnivalSubtrees(self, root):
        self.unival_subtrees = 0
        self.dfs(root)
        return self.unival_subtrees

