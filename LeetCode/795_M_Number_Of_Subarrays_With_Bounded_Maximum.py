from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countSubarrays(bound):
            count = 0
            curr = 0
            for num in nums:
                if num <= bound:
                    curr += 1
                    count += curr
                else: curr = 0
            return count
        
        return countSubarrays(right) - countSubarrays(left - 1)