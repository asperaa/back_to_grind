"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""572. Subtree of Another Tree [T - O(m+n), S - O(m+n)]
"""
import hashlib

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:


    def hash_(self, x):
        m = hashlib.sha1()
        m.update(str.encode(x))
        return m.hexdigest()
    
    def merkle(self, node):
        if not node:
            return '#'
        node.merkle = self.hash_(self.merkle(node.left) + str(node.val)+ self.merkle(node.right))
        return node.merkle
    
    def dfs(self, s, t):
        if not s:
            return False
        if s.merkle == t.merkle:
            return True
        left_dfs = self.dfs(s.left, t)
        right_dfs = self.dfs(s.right, t)
        return left_dfs or right_dfs

    def isSubtree(self, s, t):
        self.merkle(s)
        self.merkle(t)
        return self.dfs(s, t)