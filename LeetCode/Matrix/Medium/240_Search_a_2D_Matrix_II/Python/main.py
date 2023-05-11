
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row, column = 0, m - 1
        for i in range(n+m-1):
            ptr = matrix[row][column]
            if ptr > target:
                if column == 0:
                    return False
                column -= 1
                continue
            if ptr < target:
                if row == n - 1:
                    return False
                row += 1
                continue
            if ptr == target:
                return True
        return False
