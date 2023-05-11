
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1) + 1, len(nums2) + 1
        dp = [[0] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                print(dp)
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


if __name__ == "__main__":
    from tests import base_test

    base_test()
