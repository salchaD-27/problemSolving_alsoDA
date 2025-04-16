# from typing import List
# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         count = 0
#         for i in range(len(nums) - 2):
#             currDiff = nums[i + 1] - nums[i]
#             lastChecked = nums[i + 1]
#             for j in range(i + 2, len(nums)):
#                 if nums[j] == lastChecked + currDiff:
#                     count += 1
#                     lastChecked = nums[j]
#         return count
    
from typing import List
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)] 
        total = 0
        for j in range(1, n):
            for i in range(j):
                d = nums[j] - nums[i]
                dp[j][d] += dp[i][d] + 1
                total += dp[i][d] 
        return total