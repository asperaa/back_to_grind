# https://leetcode.com/problems/inorder-successor-in-bst/

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None

        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
        