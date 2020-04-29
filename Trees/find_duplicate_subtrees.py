"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""652. Find Duplicate Subtrees
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
    
    def merkle(self, root, hash_set):
        if not root:
            return '#'
        root.merkle = self.hash_(self.merkle(root.left) + str(root.val) + self.merkle(root.right))
        if root.merkle in hash_set[root.merkle]:
            hash_set[root.merkle] = (root, True)
        else:
            hash_set[root.merkle] = (root, False)
        return root.merkle
    
    def findDuplicateSubtrees(self, root):
        hash_set = {}
        duplicates = []
        self.merkle(root, hash_set)
        for node_representation, node in hash_set:
            if node[1] == True:
                duplicates.append(node[0])
        return duplicates 