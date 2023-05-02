class Solution:

    def arraySign(self, nums):
        p = 1
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                p *= -1
        return p
