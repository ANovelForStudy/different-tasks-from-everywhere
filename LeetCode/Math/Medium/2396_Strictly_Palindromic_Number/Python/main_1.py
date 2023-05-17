
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        str_n = str(n)
        if str_n != str_n[::-1]:
            return False

        l = [hex(n), oct(n), bin(n)]

        for elem in l:
            str_elem = str(elem)
            if str_elem != str_elem[::-1]:
                return False

        return True
