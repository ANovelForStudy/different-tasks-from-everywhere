
class Solution:
    def reverse(self, x: int) -> int:
        has_sign = x < 0
        s = '-' + str(x)[1:][::-1] if has_sign else str(x)[::-1]
        result = int(s)
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
