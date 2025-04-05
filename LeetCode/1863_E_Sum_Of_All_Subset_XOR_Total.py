from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        totalXOR = 0
        for mask in range(1 << len(nums)):
            subsetXOR = 0
            for i in range(len(nums)):
                if mask & (1 << i): subsetXOR ^= nums[i]
            totalXOR += subsetXOR
        return totalXOR