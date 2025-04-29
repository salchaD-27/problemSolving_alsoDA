# from typing import List
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         prefixSums = [0] * len(nums)
#         prefixSums[0] = nums[0]
#         for i in range(1, len(nums)):
#             prefixSums[i] = prefixSums[i - 1] + nums[i]
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 subSum = prefixSums[j] - (prefixSums[i - 1] if i > 0 else 0)
#                 if subSum % k == 0: return True
#         return False

from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  # remainder:index
        total = 0
        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2: return True
            else: remainder_map[remainder] = i
        return False