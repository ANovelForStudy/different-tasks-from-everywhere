
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for elem in set(nums):
            result[elem] = 0

        for elem in nums:
            result[elem] += 1

        result = list(
            dict(sorted(result.items(), key=lambda item: item[1])).items())[::-1]

        l = []
        for i in range(k):
            l.append(result[i][0])

        return l
