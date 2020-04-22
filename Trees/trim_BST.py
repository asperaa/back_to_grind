"""We are the captains of our ships, and we stay 'till the end. We our stories through.
"""

"""669. Trim a Binary Search Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def trimBST(self, root, L, R):
        if not root:
            return None
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        if root.val < L:
            root = root.right
        elif root.val > R:
            root = root.left
        return root

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    s = Solution()
    new = s.trimBST(root, 1, 2)
    print(new.left)
    