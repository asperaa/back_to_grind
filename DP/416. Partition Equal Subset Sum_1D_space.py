"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""416. Partition Equal Subset Sum [Bottom UP]
"""

class Solution:

    def subset_sum_helper(self, arr, s):
        length = len(arr)
        dp = [False for _ in range(s+1)]
        dp[0] = True
        for i in range(1, length+1):
            for j in range(s, 0, -1):
                if j >= arr[i-1]:
                    dp[j] = dp[j] or dp[j-arr[i-1]]
        return dp[s]
    
    def canPartition(self, arr):
        summ = sum(arr)
        if summ % 2 == 1:
            return False
        return self.subset_sum_helper(arr, summ // 2)