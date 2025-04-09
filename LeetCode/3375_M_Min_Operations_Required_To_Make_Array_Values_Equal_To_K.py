from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k: return -1
        nums = sorted(set(nums), reverse=True)
        if nums[-1] == k: return len(nums) - 1
        else: return len(nums)