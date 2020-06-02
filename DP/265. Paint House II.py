"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""265. Paint House II
"""

class Solution:

    def minCostII(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = grid
        for i in range(m-2, -1, -1):
            min_arr = self.minify(dp[i+1])
            for j in range(n-1, -1, -1):
                dp[i][j] = grid[i][j] + min_arr[j]
        min_cost = min(dp[0])
        return min_cost
    
    def minify(self, arr):
        n = len(arr)
        minn = second_min = float('inf')
        min_index = 0
        for i in range(n):
            if arr[i] < minn:
                second_min = minn
                minn = arr[i]
                min_index = i
            elif arr[i] < second_min and arr[i] != minn:
                second_min = arr[i]
        count = 0
        new_arr = [0]*n
        for i in range(n):
            new_arr[i] = minn
            if arr[i] == minn:
                count += 1
        if count == 1:
            new_arr[min_index] = second_min
        return new_arr

