"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""508. Most Frequent Subtree Sum
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, freq):
        if not root:
            return 0
        summ = root.val + self.dfs(root.left, freq) + self.dfs(root.right, freq)
        freq[summ] = freq.get(summ, 0) + 1
        return summ
    
    def findFrequentTreeSum(self, root):
        if not root:
            return []
        freq = {}
        self.dfs(root, freq)
        max_count = max(freq.values())
        freq_sums = [summ for summ, count in freq.items() if count == max_count]
        return freq_sums   
        