"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1130. Minimum Cost Tree From Leaf Values
"""

class Solution:
    
    def mctFromLeafValues(self, arr):
        m = len(arr)
        dp = [[None for _ in range(m+1)]for _ in range(m+1)]
        min_summ, max_leaf = self.helper(arr, 0, m-1, dp)
        return min_summ

    def helper(self, arr, i, j, dp):
        if dp[i][j]:
            return dp[i][j]
        if i == j:
            return 0, arr[i]
        if i > j:
            return 0, 0
        minn_summ = float('inf')
        for k in range(i, j):
            non_leaf_sum_left, max_leaf_val_left = self.helper(arr, i, k, dp)
            non_leaf_sum_right, max_leaf_val_right = self.helper(arr, k+1, j, dp)
            non_leaf_sum = non_leaf_sum_left + non_leaf_sum_right + max_leaf_val_left * max_leaf_val_right
            minn_summ = min(minn_summ, non_leaf_sum)
        dp[i][j] = (minn_summ, max(max_leaf_val_left, max_leaf_val_right))
        return dp[i][j]
        