from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRobWithCapability(x):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= x:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        
        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) // 2
            if canRobWithCapability(mid): high = mid
            else: low = mid + 1
        return low