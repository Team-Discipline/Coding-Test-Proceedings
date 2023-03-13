"""
https://leetcode.com/problems/house-robber/
House Robber
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums) + 1)]
        dp[1] = nums[0]
        maxval = dp[1]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[:i - 1]) + nums[i - 1]
            maxval = max(maxval, dp[i])
        return maxval


s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
