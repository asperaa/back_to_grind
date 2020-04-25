"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""687. Longest Univalue Path
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def path_helper(self, root):
        if not root:
            return 0
        if root.left:
            if root.val == root.left.val:
                left_path = 1 + self.path_helper(root.left)
            else:
                left_path = self.path_helper(root.left)
        if root.right:
            if root.val == root.right.val:
                right_path = 1 + self.path_helper(root.right)
            else:
                right_path = self.path_helper(root.right)
        if root.left and root.right:
            if root.val == root.left.val and root.val == root.right.val:
                self.long_path_length = max(self.long_path_length, right_path + left_path)
                return max(left_path, right_path)
        if root.right and root.val == root.right.val:
            self.long_path_length = max(self.long_path_length, right_path)    
            return right_path
        if root.left and root.val == root.left.val:
            self.long_path_length = max(self.long_path_length, left_path)
            return left_path
        else:
            return 0



    def longestUnivaluePath(self, root):
        self.long_path_length = 0
        self.path_helper(root)
        return self.long_path_length