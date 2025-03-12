from typing import List
from bisect import bisect_left
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_non_neg = bisect_left(nums, 0)
        first_pos = bisect_left(nums, 1)
        neg_count = first_non_neg
        pos_count = len(nums) - first_pos
        return max(neg_count, pos_count)