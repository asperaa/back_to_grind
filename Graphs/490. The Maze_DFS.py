"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""490. The Maze [DFS]
"""

class Solution:

    def hasPath(self, grid, start, dest):
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)]for _ in range(m)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        sr, sc = start
        dr, dc = dest

        def dfs(i, j, grid, visited):
            if visited[i][j]:
                return False
            if i == dr and j == dc:
                return True
            visited[i][j] = True
            for delta_x, delta_y in directions:
                x = i + delta_x
                y = j + delta_y
                while 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    x += delta_x
                    y += delta_y
                if dfs(x-delta_x, y-delta_y, grid, visited):
                    return True
            return False
        
        dfs(sr, sc)