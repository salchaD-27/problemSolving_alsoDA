from typing import List
from functools import lru_cache
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        def average(i, j): return (prefix[j] - prefix[i]) / (j - i)

        @lru_cache(maxsize=None)
        def dp(i, k):
            if k == 1: return average(i, n)
            max_score = 0
            for j in range(i + 1, n - k + 2):
                max_score = max(max_score, average(i, j) + dp(j, k - 1))
            return max_score
        return dp(0, k)