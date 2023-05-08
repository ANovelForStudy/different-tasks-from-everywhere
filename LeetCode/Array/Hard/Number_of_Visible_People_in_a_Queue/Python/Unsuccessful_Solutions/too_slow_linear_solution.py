
# The maximum distance reached is 31 tests :(
# Complexity: O(N^2)

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result_list: List[int] = []
        continue_it: bool = False

        for index_dude, dude in enumerate(heights):
            result: int = 0
            persons_between_max: int = 0

            for index_target, target in enumerate(heights[index_dude+1:]):

                if target > dude:
                    result += 1
                    continue_it = True
                    break
                if target > persons_between_max and dude > persons_between_max:
                    result += 1

                if target > persons_between_max:
                    persons_between_max = target

            result_list.append(result)

            if continue_it:
                continue

        return result_list
