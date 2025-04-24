# from typing import List
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         count = 0
#         def backtrack(index: int, total: int):
#             nonlocal count
#             if index == len(nums):
#                 if total == target: count += 1
#                 return
#             backtrack(index + 1, total + nums[index])
#             backtrack(index + 1, total - nums[index])
#         backtrack(0, 0)
#         return count

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # if possible to partition
        if (target + total) % 2 != 0 or abs(target) > total: return 0
        subset_sum = (target + total) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[subset_sum]