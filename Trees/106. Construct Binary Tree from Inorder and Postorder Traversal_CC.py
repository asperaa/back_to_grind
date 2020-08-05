"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""106. Construct Binary Tree from Inorder and Postorder Traversal [CC]
"""

class Solution(object):
    def __init__(self):
        self.length = 0
        self.idx = self.length - 1
    
    def bt_util(self, inorder, postorder, book, left, right):
        if left > right:
            return None
        root = TreeNode(postorder[self.idx])
        partition_idx = book[postorder[self.idx]]
        self.idx -= 1
        root.right = self.bt_util(inorder, postorder, book, partition_idx + 1, right)
        root.left = self.bt_util(inorder, postorder, book, left, partition_idx - 1)
        return root
        
        
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        book = {val:idx for idx, val in enumerate(inorder)}
        self.length = len(inorder)
        return self.bt_util(inorder, postorder, book, 0, self.length - 1)
