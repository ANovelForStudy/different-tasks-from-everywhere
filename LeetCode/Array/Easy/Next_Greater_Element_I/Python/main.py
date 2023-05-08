
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []
        stack = []
        greater_numbers = {}

        for num in nums2:
            while stack and num > stack[-1]:
                greater_numbers[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            if num in greater_numbers:
                result.append(greater_numbers[num])
            else:
                result.append(-1)

        return result
