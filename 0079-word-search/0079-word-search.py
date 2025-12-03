# Time Complexity : O(n * m *  4 ^ K)
# n : row, m : col, k : length of the word

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        COLS, ROWS = len(board[0]), len(board)
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True


            if (min(row, col) < 0 or
                row >= ROWS or col >= COLS or (row, col) in path):
                return False

            elif row < ROWS and col < COLS and word[i] != board[row][col]:
                return False

            path.add((row, col))

            res = (dfs(row + 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row-1, col, i +1) or dfs(row, col-1, i + 1))

            path.remove((row, col))

            return res

    
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False






