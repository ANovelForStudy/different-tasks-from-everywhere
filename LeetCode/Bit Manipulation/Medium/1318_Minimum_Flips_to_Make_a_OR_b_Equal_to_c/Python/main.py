
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        if a | b == c:
            return 0

        count = 0
        while a > 0 or b > 0 or c > 0:
            last_bit_a = a & 1
            last_bit_b = b & 1
            last_bit_c = c & 1

            if last_bit_c == 0:
                count += last_bit_a + last_bit_b
            else:
                if last_bit_a == 0 and last_bit_b == 0:
                    count += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return count
