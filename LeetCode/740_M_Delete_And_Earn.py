from typing import List
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        count = Counter(nums)
        max_num = max(nums)
        dp = [0] * (max_num + 1)
        dp[1] = count[1] * 1
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * count[i])
        return dp[max_num]