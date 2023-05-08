
from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = []
        stack = []
        peoples = 0
        for height in heights[::-1]:
            if not stack:
                stack.append(height)
                peoples += 1
                result.append(0)
            else:
                while stack and height > stack[-1]:
                    stack.pop()
                    peoples += 1
                if not stack:
                    peoples -= 1
                stack.append(height)
                result.append(peoples)
                peoples = 1

        return result[::-1]
