# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_area, curr_area = 0, 0  
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            area = 1 

            while q:
                row, col = q.popleft()
                for dr, dc in directions:    
                    new_row, new_col = row + dr, col + dc
                    if (new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS or grid[new_row][new_col] == 0):
                        continue 
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = 0 
                    area += 1
            return area
                        

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    curr_area = bfs(row, col)
                    max_area = max(max_area, curr_area)        
        
        return max_area