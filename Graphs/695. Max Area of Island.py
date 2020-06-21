"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""695. Max Area of Island
"""

class Solution:
    
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        maxx = 0
        m, n = len(grid), len(grid[0])
        self.curr_area = 0
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return
            self.curr_area += 1
            grid[i][j] = 2
            dfs(i+1, j, grid)
            dfs(i-1, j, grid)
            dfs(i, j-1, grid)
            dfs(i, j+1, grid)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.curr_area = 0
                    dfs(i, j, grid)
                    maxx = max(maxx, self.curr_area)
        return maxx