# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# DFS version
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
#         ROWS, COLS = len(grid), len(grid[0])
#         islands = 0 

#         def dfs(row, col):
#             if (row < 0 or col < 0 or row >= ROWS or col >= COLS or
#                 grid[row][col] == "0"):
#                 return 

#             grid[row][col] = "0"
#             for dr, dc in directions:
#                 dfs(row + dr, col + dc)

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1":
#                     dfs(r, c)
#                     islands += 1
        
#         return islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS or grid[new_row][new_col] == "0":
                        continue
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands

