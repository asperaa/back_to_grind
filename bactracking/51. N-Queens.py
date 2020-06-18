"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""51. N-Queens
"""

class Solution:
    
    def solveNQueens(self, n):
        chess = [['.' for _ in range(n)]for _ in range(n)]
        self.ans = []
        self.n = n
        for j in range(n):
            chess[0][j] = "Q"
            self.helper(chess, 1)
            chess[0][j] = "."
        return self.ans
    
    def helper(self, chess, i):
        if i == self.n:
            # print(chess, i)
            self.ans.append(chess)
            print(self.ans)
            return
        for j in range(self.n):
            if self.is_valid(chess, i, j):
                chess[i][j] = "Q"
                self.helper(chess, i+1)
                # print(chess, i)
                chess[i][j] = "."
    
    def is_valid(self, chess, x, y):
        for i in range(x):
            for j in range(self.n):
                if chess[i][j] == 'Q' and (j == y or abs(i-x) == abs(j-y)):
                    return False
        return True
