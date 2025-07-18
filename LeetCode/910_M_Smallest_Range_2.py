# from typing import List
# class Solution:
#     def smallestRangeII(self, nums: List[int], k: int) -> int:
#         return (max(nums)-k)-(min(nums)+k)

from typing import List
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[-1] - nums[0]
        for i in range(n - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i+1] - k)
            res = min(res, high - low)
        return res