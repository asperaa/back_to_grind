"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""653. Two Sum IV - Input is a BST [DFS]
"""

from collections import deque
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, root, k, hash_set):
        if not root:
            return
        if k - root.val in hash_set:
            self.ans = True
            return
        hash_set.add(root.val)
        self.dfs(root.left, k, hash_set)
        self.dfs(root.right, k, hash_set)

    def findTarget(self, root, k):
        self.ans = False
        hash_set = set()
        self.dfs(root, k, hash_set)
        return self.ans
    
    def findTarget_BFS(self, root, k):
        if not root:
            return False
        hash_set, queue = set(), deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if k - node.val in hash_set:
                return True
            hash_set.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
    
    def findTarget_Inorder_helper(self, root, ordered_array):
        if root:
            self.findTarget_Inorder_helper(root.left, ordered_array)
            ordered_array.append(root.val)
            self.findTarget_Inorder_helper(root.right, ordered_array)


    def findTarget_Inorder(self, root, k):
        if not root:
            return False
        ordered_array = []
        self.findTarget_Inorder_helper(root, ordered_array)

        l, r = 0, len(ordered_array) - 1
        while l < r:
            if ordered_array[l] + ordered_array[r] == k:
                return True
            elif ordered_array[l] + ordered_array[r] < k:
                l += 1
            else:
                r -= 1
        return False

