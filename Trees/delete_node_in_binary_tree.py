# https://leetcode.com/problems/delete-node-in-a-bst/
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

                
        def find_inorder_successor(root):
            current = root
            inorder_successor= 0
            while current:
                inorder_successor = current.val
                current = current.left
            return inorder_successor
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:

            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            else:
                root.val = find_inorder_successor(root.right)


                root.right = self.deleteNode(root.right, root.val)
        
        
        
        return root