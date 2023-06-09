
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid_index = (l + r) // 2
            mid = letters[mid_index]

            if mid <= target:
                l = mid_index + 1

            if mid > target:
                if letters[mid_index - 1] <= target:
                    return mid
                else:
                    r = mid_index - 1

        return letters[0]
