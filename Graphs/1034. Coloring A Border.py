"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1034. Coloring A Border
"""

class Solution:

    def colorBorder(self, grid, r0, c0, new_color):
        m, n = len(grid), len(grid[0])
        old_color = grid[r0][c0]
        
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != old_color:
                return
            grid[i][j] = -1
            dfs(i+1, j, grid)
            dfs(i-1, j, grid)
            dfs(i, j-1, grid)
            dfs(i, j+1, grid)
        
        dfs(r0, c0, grid)
        for i in range(m):
            if grid[i][0] == -1:
                grid[i][0] = -2
            if grid[i][n-1] == -1:
                grid[i][n-1] = -2
        for j in range(n):
            if grid[0][j] == -1:
                grid[0][j] = -2
            if grid[m-1][j] == -1:
                grid[m-1][j] = -2
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == -1 and (grid[i-1][j] > 0 or grid[i+1][j] > 0 or grid[i][j-1] > 0 or grid[i][j+1] > 0):
                    grid[i][j] = -2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -2:
                    grid[i][j] = new_color
                elif grid[i][j] == -1:
                    grid[i][j] = old_color
        return grid