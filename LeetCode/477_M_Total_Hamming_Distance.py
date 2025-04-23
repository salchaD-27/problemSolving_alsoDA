from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(32):
            count_ones = sum((num >> i) & 1 for num in nums)
            count_zeros = n - count_ones
            total += count_ones * count_zeros
        return total