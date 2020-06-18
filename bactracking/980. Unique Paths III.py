"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""980. Unique Paths III
"""

class Solution:
    
    def uniquePathsIII(self, grid):
        self.ans = 0
        empty = 0
        x, y = 0, 0
        m, n = len(grid), len(grid[0])
        self.m = m
        self.n = n
        visited = [[False for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] == 0:
                    empty += 1
        self.empty = empty
        self.helper(grid, x, y, 0, visited)
        return self.ans

    def helper(self, grid, i, j, curr_empty, visited):
        if not self.is_valid(grid, i, j, visited):
            return
        if grid[i][j] == 2 and curr_empty == self.empty + 1:
            self.ans += 1
            return
        visited[i][j] = True
        self.helper(grid, i+1, j, curr_empty + 1, visited)
        self.helper(grid, i-1, j, curr_empty + 1, visited)
        self.helper(grid, i, j+1, curr_empty + 1, visited)
        self.helper(grid, i, j-1, curr_empty + 1, visited)
        visited[i][j] = False
    
    def is_valid(self, grid, i, j, visited):
        if 0 <= i and i < self.m and 0 <= j  and j < self.n and not visited[i][j] and grid[i][j] >= 0:
            return True
        return False
