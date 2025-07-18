# from typing import List
# class Solution:
#     def partitionDisjoint(self, nums: List[int]) -> int:
#         leftMax=nums[0]
#         splitIdx=0
#         for i in range(1, len(nums)):
#             if leftMax<max(nums[i:]): return splitIdx+1
#             leftMax=max(leftMax,nums[i])
#             splitIdx=i

from typing import List
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        minRight = [0] * n
        minRight[-1] = nums[-1]
        # suffix mins
        for i in range(n - 2, -1, -1):
            minRight[i] = min(nums[i], minRight[i + 1])
        leftMax = nums[0]
        for i in range(n - 1):
            if leftMax <= minRight[i + 1]: return i + 1
            leftMax = max(leftMax, nums[i])
        return -1