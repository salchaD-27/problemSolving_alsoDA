# for sorted arr, any num at idx i appears in:
#   2^i subsets as max
#   2^(n - i - 1) subsets as min
from typing import List
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = pow2[i - 1] * 2 % MOD
        res = 0
        for i in range(n):
            max_contrib = pow2[i]
            min_contrib = pow2[n - i - 1]
            res = (res + nums[i] * (max_contrib - min_contrib)) % MOD
        return res