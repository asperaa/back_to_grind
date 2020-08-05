"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""105. Construct Binary Tree from Preorder and Inorder Traversal [CC]
"""

class Solution:
    def __init__(self):
        self.idx = 0
    
    def bt_util(self, preorder, inorder, book, left, right):
        if left > right:
            return None
        root = TreeNode(preorder[self.idx])
        partition_index = book[preorder[self.idx]]
        self.idx += 1
        root.left = self.bt_util(preorder, inorder, book, left, partition_index-1)
        root.right = self.bt_util(preorder, inorder, book, partition_index+1, right)
        return root
        
    
    
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        book = {val: idx for idx, val in enumerate(inorder)}
        return self.bt_util(preorder, inorder, book, 0, len(inorder)-1)
        