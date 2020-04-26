"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""108. Convert Sorted Array to Binary Search Tree
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def convert(self, arr, l, r):
        if l > r:
            return None
        mid = (l+r) // 2
        node = TreeNode(arr[mid])
        node.left = self.convert(arr, l, mid-1)
        node.right = self.convert(arr, mid+1, r)
        return node
    
    def sortedArrayToBST(self, arr):
        return self.convert(arr, 0, len(arr)-1)