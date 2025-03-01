# from typing import List
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         if len(nums) < 2: return len(nums)
#         dp = [1] * len(nums)
#         dp[1] = 2 if nums[1] != nums[0] else 1
#         last = 0 if nums[1] < nums[0] else 1 
#         for i in range(2, len(nums)):
#             if last == 0 and nums[i] > nums[i - 1]:  
#                 dp[i] = dp[i - 1] + 1
#                 last = 1
#             elif last == 1 and nums[i] < nums[i - 1]:
#                 dp[i] = dp[i - 1] + 1
#                 last = 0
#             else: dp[i] = dp[i - 1]
#         return dp[-1]

from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        prev_diff = nums[1] - nums[0]
        count = 1 if prev_diff == 0 else 2
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (prev_diff <= 0 and diff > 0) or (prev_diff >= 0 and diff < 0):
                count += 1
                prev_diff = diff
        return count