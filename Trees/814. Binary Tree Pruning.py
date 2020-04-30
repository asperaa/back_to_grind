"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""814. Binary Tree Pruning
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def pruneTree(self, root):
        if not root:
            return
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            root = None
        return root


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    s = Solution()
    root = s.pruneTree(root)
    print(root.left.left)