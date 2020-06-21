"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1254. Number of Closed Islands
"""

class Solution:

    def closedIsland(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 0:
                return
            grid[i][j] = 2
            dfs(i+1, j, grid)
            dfs(i-1, j, grid)
            dfs(i, j-1, grid)
            dfs(i, j+1, grid)
        
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0, grid)
            if grid[i][n-1] == 0:
                dfs(i, n-1, grid)
        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j, grid)
            if grid[m-1][j] == 0:
                dfs(m-1, j, grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, grid)
                    ans += 1
        return ans
                