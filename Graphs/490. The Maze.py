"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""490. The Maze
"""

from collections import deque

from collections import deque

class Solution:

    def hasPath(self, grid, start, destination):
        m, n  = len(grid), len(grid[0])
        sr, sc = start
        dr, dc = destination
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for _ in range(n)]for _ in range(m)]
        queue = deque()
        queue.append((sr, sc))
        visited[sr][sc] = True
        while queue:
            i, j = queue.popleft()
            if i == dr and j == dc:
                return True
            for delta_x, delta_y in directions:
                x = i + delta_x
                y = j + delta_y
                # Rolling
                while 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    x += delta_x
                    y += delta_y
                if not visited[x - delta_x][y - delta_y]:
                    queue.append((x-delta_x, y-delta_y))
                    visited[x-delta_x][y-delta_y] = True
        return False
        