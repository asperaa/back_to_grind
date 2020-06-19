"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""37. Sudoku Solver
"""

class Solution:

    def solveSudoku(self, board):
        self.solve(board)
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for ch in "123456789":
                        if self.is_valid(board, i, j, ch):
                            board[i][j] = ch
                            if self.solve(board):
                                return True
                            board[i][j] = "."
                    return False
        return True
    
    def is_valid(self, board, row, col, ch):
        square_row = 3 * (row//3)
        square_col = 3 * (col//3)
        for i in range(9):
            if board[i][col] == ch or board[row][i] == ch:
                return False
            if board[square_row + i // 3][square_col + i % 3] == ch:
                return False
        return True