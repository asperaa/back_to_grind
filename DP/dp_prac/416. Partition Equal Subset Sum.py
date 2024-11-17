class Solution:
    
    def subset_sum_helper(self, arr, s):
        length = len(arr)
        dp = [[None for _ in range(s+1)] for _ in range(length+1)]
        for i in range(length+1):
            dp[i][0] = True
        for j in range(1, s+1):
            dp[0][j] = False
        for i in range(1, length+1):
            for j in range(1, s+1):
                if j >= arr[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[length][s]

    def canPartition(self, arr):
        summ = sum(arr)
        if summ % 2 == 1:
            return False
        return self.subset_sum_helper(arr, summ // 2)