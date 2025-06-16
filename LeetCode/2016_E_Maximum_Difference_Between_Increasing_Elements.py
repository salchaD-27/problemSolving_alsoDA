from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res=-1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]: res=max(res, nums[j]-nums[i])
        return res

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1
        for num in nums[1:]:
            if num > min_val: max_diff = max(max_diff, num - min_val)
            else: min_val = num
        return max_diff