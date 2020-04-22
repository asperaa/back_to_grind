"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""110. Balanced Binary Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def is_balanced_helper(self, root):
        if not root:
            return (0, True)
        left_height, left_balanced = self.is_balanced_helper(root.left)
        right_height, right_balanced = self.is_balanced_helper(root.right)
        is_balanced = abs(left_height-right_height) <= 1 and left_balanced and right_balanced
        return (max(1 + left_height, 1 + right_height), is_balanced)
    
    def isBalanced(self, root):
        height, balanced = self.is_balanced_helper(root)
        print(height)
        return balanced

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right.right.right = TreeNode(4)
    s = Solution()
    print(s.isBalanced(root))