"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""652. Find Duplicate Subtrees [Built-in Hash]
"""

from collections import defaultdict

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def findDuplicateSubtrees(self, root):
        duplicate_subtrees = []
        self.subtree_hash = defaultdict(int)
        self.dfs(root, duplicate_subtrees)
        return duplicate_subtrees
    
    def dfs(self, root, duplicate_subtrees):
        if not root:
            return '#'.encode()
        subtree_hash_val = hash(
            self.dfs(root.left, duplicate_subtrees) 
            + str(root.val).encode()
            + self.dfs(root.right, duplicate_subtrees)
            )
        subtree_hash_val = str(subtree_hash_val).encode()
        if self.subtree_hash[subtree_hash_val] == 1:
            duplicate_subtrees.append(root)
        self.subtree_hash[subtree_hash_val] += 1
        return subtree_hash_val 


