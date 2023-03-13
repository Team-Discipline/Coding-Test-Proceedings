"""
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/
Maximum Score from Performing Multiplication Operations
"""
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [0] * (m + 1)

        for i in range(m - 1, -1, -1):
            nextRow = dp.copy()
            # Present Row is now nextRow, since iterating upwards

            for left in range(i, -1, -1):
                dp[left] = max(multipliers[i] * nums[left] + nextRow[left + 1],
                               multipliers[i] * nums[n - 1 - (i - left)] + nextRow[left])

        return dp[0]


s = Solution()
assert s.maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]) == 102
