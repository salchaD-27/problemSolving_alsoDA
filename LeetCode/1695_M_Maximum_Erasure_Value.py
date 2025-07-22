from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        max_score = curr_sum = 0
        start = 0
        for end in range(len(nums)):
            while nums[end] in seen:
                seen.remove(nums[start])
                curr_sum -= nums[start]
                start += 1
            seen.add(nums[end])
            curr_sum += nums[end]
            max_score = max(max_score, curr_sum)
        return max_score