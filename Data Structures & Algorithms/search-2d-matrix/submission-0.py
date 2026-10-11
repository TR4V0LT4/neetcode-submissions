class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # old_row = matrix[0]
        for row in range(len(matrix)):
            for i in range(len(matrix[row])):
                if matrix[row][i] == target:
                    return True
        return False






        