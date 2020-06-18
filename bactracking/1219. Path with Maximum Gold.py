"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1219. Path with Maximum Gold
"""

class Solution:

    def getMaximumGold(self, grid):
        self.maxx = float('-inf')
        m, n = len(grid), len(grid[0])
        self.m = m
        self.n = n
        visited = [[False for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.helper(grid, i, j, 0, visited)
        return self.maxx
    
    def helper(self, grid, i, j, curr_summ, visited):
        if not self.is_valid(grid, i, j, visited):
            self.maxx = max(self.maxx, curr_summ)
            return
        visited[i][j] = True
        self.helper(grid, i+1, j, curr_summ + grid[i][j], visited)
        self.helper(grid, i-1, j, curr_summ + grid[i][j], visited)
        self.helper(grid, i, j+1, curr_summ + grid[i][j], visited)
        self.helper(grid, i, j-1, curr_summ + grid[i][j], visited)
        visited[i][j] = False
    
    def is_valid(self, grid, i, j, visited):
        if i >= 0 and j >= 0 and i < self.m and j < self.n and not visited[i][j] and grid[i][j] != 0:
            return True
        return False