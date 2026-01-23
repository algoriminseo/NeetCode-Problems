class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros.append((row, col))
        while zeros:
            zrow, zcol = zeros.pop()
            for r in range(len(matrix)):
                if r != zrow:
                    matrix[r][zcol] = 0 
            for c in range(len(matrix[0])):
                if c != zcol:
                    matrix[zrow][c] = 0 
        return matrix

        
