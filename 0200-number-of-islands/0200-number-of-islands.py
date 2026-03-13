class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1, 0],[0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        
        islands = 0

        def dfs(row, col):
            nonlocal islands

            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0"):
                return 

            grid[row][col] = "0"
            
            for nr, nc in directions:
                dfs(row + nr, col + nc)

        for ROW in range(ROWS):
            for COL in range(COLS):
                if grid[ROW][COL] == "1":
                    islands += 1
                    dfs(ROW, COL)

        return islands






