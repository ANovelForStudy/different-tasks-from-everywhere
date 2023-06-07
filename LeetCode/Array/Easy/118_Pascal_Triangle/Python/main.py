
from typing import List


class Solution:
    def generate(self, nums_rows: int) -> List[List[int]]:

        triangle = [[1], [1, 1]]

        if nums_rows < 3:
            return triangle[:nums_rows]

        for _ in range(nums_rows - 2):

            new_row = [1]

            for i in range(1, len(triangle[-1])):
                new_row.append(triangle[-1][i] + triangle[-1][i-1])

            new_row.append(1)

            triangle.append(new_row)

        return triangle
