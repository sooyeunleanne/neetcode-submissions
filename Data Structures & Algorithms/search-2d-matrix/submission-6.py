class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        left, right = 0, ROWS * COLS - 1
        while left <= right:
            mid = (left + right) // 2

            row = (mid // COLS)
            col = (mid % COLS)

            cur = matrix[row][col]
            if cur == target:
                return True
            if cur < target:
                left = mid + 1
            elif cur > target:
                right = mid - 1
               
        return False   