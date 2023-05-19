
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = (bin(x)[2::])[::-1]
        bin_y = (bin(y)[2::])[::-1]

        len_x = len(bin_x)
        len_y = len(bin_y)

        result = 0

        if len_x > len_y:
            bin_y += "0" * (len_x - len_y)
        elif len_y > len_x:
            bin_x += "0" * (len_y - len_x)

        for i, j in zip(bin_y, bin_x):
            if i != j:
                result += 1

        return result
