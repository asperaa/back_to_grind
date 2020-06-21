"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1020. Number of Enclaves
"""

class Solution:

    def dfs(self, i, j, grid):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] != 1:
            return
        grid[i][j] = 2
        self.dfs(i+1, j, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i, j+1, grid)

    def numEnclaves(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        self.m = m
        self.n = n
        res = 0
        for i in range(m):
            if grid[i][0] == 1:
                self.dfs(i, 0, grid)
            if grid[i][n-1] == 1:
                self.dfs(i, n-1, grid)
        for j in range(n):
            if grid[0][j] == 1:
                self.dfs(0, j, grid)
            if grid[m-1][j] == 1:
                self.dfs(m-1, j, grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
        return res

        
