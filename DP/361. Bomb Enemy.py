"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""361. Bomb Enemy
"""

class Solution:
    
    def maxKilledEnemies(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        hor = [[0 for _ in range(n+1)]for _ in range(m)]
        ver = [[0 for _ in range(n)]for _ in range(m+1)]
        maxx = 0
        for i in range(m):
            count = 0
            for j in range(n):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    hor[i][j] = count
                    count = 0
            hor[i][n] = count
            count = hor[i][n]
            for j in range(n-1, -1, -1):
                if grid[i][j] == '0':
                    hor[i][j] = count
                elif grid[i][j] == 'W':
                    count = hor[i][j]

        for j in range(n):
            count = 0
            for i in range(m):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    ver[i][j] = count
                    count = 0
            ver[m][j] = count
            count = ver[m][j]
            for i in range(m-1, -1, -1):
                if grid[i][j] == '0':
                    ver[i][j] = count
                elif grid[i][j] == 'W':
                    count = ver[i][j]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    maxx = max(maxx, hor[i][j] + ver[i][j])
        return maxx