
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = sorted(list(set(nums)))
        for i, item in enumerate(uniq):
            nums[i] = item
        return len(uniq)
