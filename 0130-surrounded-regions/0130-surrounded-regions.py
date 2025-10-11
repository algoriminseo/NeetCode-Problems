# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        count = 0
        res = board.copy()
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(board, r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
            board[r][c] != "O"):
                return 

            board[r][c] = "T"
            dfs(board, r + 1, c)
            dfs(board, r - 1, c)
            dfs(board, r, c + 1)
            dfs(board, r, c - 1)


        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(board, r, 0)
            if board[r][COLS-1] == "O":
                dfs(board, r, COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(board, 0, c)
            if board[ROWS-1][c] == "O":
                dfs(board, ROWS-1, c)
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

        return None