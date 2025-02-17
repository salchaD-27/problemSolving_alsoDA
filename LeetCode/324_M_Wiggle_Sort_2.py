import math
from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = math.ceil(len(nums) / 2)
        left = nums[:mid][::-1]
        right = nums[mid:][::-1]
        nums[:] = [val for pair in zip(left, right) for val in pair] + left[len(right):]