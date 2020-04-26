"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""538. Convert BST to Greater Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def convert_helper(self, root):
        if not root:
            return
        self.convert_helper(root.right)
        self.total +=  root.val
        root.val = self.total
        self.convert_helper(root.left)
        return root
    
    def convertBST(self, root):
        self.total = 0
        return self.convert_helper(root)

if __name__ == "__main__":
     root = TreeNode(2)
     root.left = TreeNode(0)
     root.right = TreeNode(3)
     root.left.left = TreeNode(-4)
     root.left.right = TreeNode(1)
     s = Solution()
     print(s.convertBST(root))