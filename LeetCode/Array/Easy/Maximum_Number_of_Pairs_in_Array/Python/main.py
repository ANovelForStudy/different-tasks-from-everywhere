
from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        result = [0, 0]
        for element, quantity in nums.items():
            result[0] += quantity // 2
            result[1] += quantity % 2
        return result
