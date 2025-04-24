from typing import List
from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        total_unique = len(set(nums))
        for L in range(len(nums)):
            sub_count = Counter()
            unique = 0
            for R in range(L, len(nums)):
                if sub_count[nums[R]] == 0: unique += 1
                sub_count[nums[R]] += 1
                if unique == total_unique: count += 1
        return count