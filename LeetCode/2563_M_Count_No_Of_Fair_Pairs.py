import bisect
from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n):
            low = lower - nums[i]
            high = upper - nums[i]
            left = bisect.bisect_left(nums, low, i + 1, n)
            right = bisect.bisect_right(nums, high, i + 1, n)
            count += (right - left)
        return count