class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2

            row = matrix[mid_row]

            if row[0] == target or row[-1] == target:
                return True
            elif row[0] > target:
                bottom = mid_row - 1
            elif row[-1] < target:
                top = mid_row + 1
            elif row[0] < target < row[-1]:
                left, right = 0, len(row) - 1
                while left <= right:
                    mid_col = (left + right) // 2
                    if row[mid_col] == target:
                        return True
                    elif target > row[mid_col]:
                        left = mid_col + 1
                    elif target < row[mid_col]:
                        right = mid_col - 1
                return False
        return False


