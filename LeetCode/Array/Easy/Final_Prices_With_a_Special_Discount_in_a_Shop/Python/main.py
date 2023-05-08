
# Solution via monotone stack

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, item in enumerate(prices):
            while stack and prices[stack[-1]] >= item:
                prices[stack.pop()] -= item
            stack.append(i)

        return prices
