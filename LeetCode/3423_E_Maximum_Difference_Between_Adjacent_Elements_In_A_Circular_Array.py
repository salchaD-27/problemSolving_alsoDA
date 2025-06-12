from typing import List
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff=float('-inf')
        for i in range(len(nums)-1):
            diff=max(diff, abs(nums[i]-nums[i+1]))
        diff=max(diff, abs(nums[-1]-nums[0]))
        return diff