"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""733. Flood Fill
"""

class Solution:
    
    def floodFill(self, grid, sr, sc, new_color):
        if not grid:
            return grid 
        m, n = len(grid), len(grid[0])
        self.new_color = new_color
        self.old_color = 0
        self.m = m
        self.n = n
        self.old_color = grid[sr][sc]
        if self.old_color == self.new_color:
            return grid
        self.dfs(sr, sc, grid)
        return grid
    
    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] != self.old_color:
            return
        grid[i][j] = self.new_color
        self.dfs(i+1, j, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i, j+1, grid)