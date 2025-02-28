# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

class Solution:
    
    
    def helper(self, i, j, arr):
        if j == 0:
            return True
        if i == 0:
            return arr[i] == j
        if self.dp[i][j]:
            return self.dp[i][j]
        not_take = self.helper(i-1, j, arr)
        take = False
        if arr[i] < j:
            take = self.helper(i-1, j-arr[i], arr)
        self.dp[i][j] = take or not_take
        return self.dp[i][j]
    
    def isSubsetSum (self, arr, target):
        m = len(arr)
        self.dp = [[None for _ in range(target+1)] for _ in range(m)]
        return self.helper(m-1, target, arr)