"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""130. Surrounded Regions
"""

class Solution:
    
    def dfs(self, i, j, board):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or board[i][j] != "O":
            return
        board[i][j] = "#"
        self.dfs(i+1, j, board)
        self.dfs(i-1, j, board)
        self.dfs(i, j-1, board)
        self.dfs(i, j+1, board)
    
    def solve(self, board):
        m, n = len(board), len(board[0])
        self.m = m
        self.n = n
        for i in range(m):
            if board[i][0] == "O":
                self.dfs(i, 0, board)
            if board[i][n-1] == "O":
                self.dfs(i, n-1, board)
        for j in range(n):
            if board[0][j] == "O":
                self.dfs(0, j, board)
            if board[m-1][j] == "O":
                self.dfs(m-1, j, board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"