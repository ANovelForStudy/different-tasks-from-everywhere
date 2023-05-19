
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x or y:
            if x & 1 != y & 1:
                result += 1
            x >>= 1
            y >>= 1
        return result
