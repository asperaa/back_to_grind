"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""200. Number of Islands
"""

class Solution:

    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        m, n = len(grid), len(grid[0])
        self.m = m
        self.n = n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    count += 1
        return count
    
    def dfs(self, i, j, grid):
        if not self.is_valid(i, j, grid):
            return
        grid[i][j] = 0
        self.dfs(i+1, j, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j+1, grid)
        self.dfs(i, j-1, grid)

    def is_valid(self, i, j, grid):
        if 0<= i < self.m and 0 <= j < self.n and grid[i][j] == "1":
            return True
        return False 