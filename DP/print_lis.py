# https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1
class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        n = len(arr)
        dp = [1 for _ in range(n)]
        store = [i for i in range(n)]
        maxx = 1
        lastIndex = 0
        for i in range(n):
            for prev in range(i):
                if arr[prev] < arr[i] and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    store[i] = prev
            if dp[i] > maxx:
                maxx = dp[i]
                lastIndex = i
                    
        ans = []
        ans.append(arr[lastIndex])
        
        while store[lastIndex]!=lastIndex:
            lastIndex = store[lastIndex]
            ans.append(arr[lastIndex])
        return ans[::-1]