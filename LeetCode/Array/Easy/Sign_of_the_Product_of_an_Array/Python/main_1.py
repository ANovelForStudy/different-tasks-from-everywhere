class Solution:
    def arraySign(self, n):
        return 0 if 0 in n else reduce(mul, [-1 if _ < 0 else 1 for _ in n])
