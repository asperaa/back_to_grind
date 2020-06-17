"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""79. Word Search
"""

class Solution:
    
    def exist(self, grid, word):
        m, n = len(grid), len(grid[0])
        self.word_length = len(word)
        self.word = word
        self.m = m
        self.n = n
        visited = [[False for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.helper(grid, i, j, 0, visited):
                    return True
        return False
    
    def helper(self, grid, i, j, index, visited):
        if index == self.word_length:
            return True
        if not self.is_valid(grid, i, j, index, visited):
            return False
        visited[i][j] = True
        if self.helper(grid, i+1, j, index+1, visited):
            return True
        if self.helper(grid, i, j+1, index+1, visited):
            return True
        if self.helper(grid, i-1, j, index+1, visited):
            return True
        if self.helper(grid, i, j-1, index+1, visited):
            return True
        visited[i][j] = False
        return False
    
    def is_valid(self, grid, i, j, index, visited):
        if i >= 0 and j >= 0 and i < self.m and j < self.n and not visited[i][j] and self.word[index] == grid[i][j]:
            return True
        return False