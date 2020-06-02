"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1289. Minimum Falling Path Sum II
"""

class Solution:
    
    def minFallingPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = grid
        for i in range(m-2, -1, -1):
            min_arr, second_min = self.minify(dp[i+1])
            for j in range(n-1, -1, -1):
                dp[i][j] = grid[i][j] + min_arr[j]
        minn_value = min(dp[0])
        return minn_value

    def minify(self, arr):
        n = len(arr)
        minn = float('inf')
        second_min = minn
        min_index = 0
        for i in range(n):
            if arr[i] < minn:
                second_min = minn
                minn = arr[i]
                min_index = i
            elif arr[i] < second_min and arr[i] != minn:
                second_min = arr[i]
        new_arr = [0] * n
        count = 0
        for i in range(n):
            new_arr[i] = minn
            if arr[i] == minn:
                count += 1
        if count == 1:
            new_arr[min_index] = second_min
        return new_arr, second_min

