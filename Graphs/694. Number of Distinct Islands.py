"""We are the captains of ur ships, and we stay 'till the end. We see our stories through.
"""

"""694. Number of Distinct Islands
"""

class Solution:

    def numDistinctIslands(self, grid):
        m, n = len(grid), len(grid[0])
        distinct_islands = set()

        def dfs(i, j, direction):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                self.shape += direction
                dfs(i-1, j, "U")
                dfs(i+1, j, "D")
                dfs(i, j-1, "L")
                dfs(i, j+1, "R")
                self.shape += "B"
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.shape = ""
                    dfs(i, j, "S")
                    distinct_islands.add(self.shape)
        return len(distinct_islands)

