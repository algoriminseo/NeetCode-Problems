class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        COLS = len(matrix[0])
        left = 0  
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // COLS   
            col = mid % COLS 
            if matrix[row][col] > target:
                right -= 1
            elif matrix[row][col] < target:
                left += 1
            else:
                return True
        return False