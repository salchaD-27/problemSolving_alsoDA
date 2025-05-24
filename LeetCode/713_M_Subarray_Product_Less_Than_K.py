# from typing import List
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         def prod(arr):
#             ans = 1
#             for num in arr:
#                 ans *= num
#             return ans
        
#         count = 0
#         n = len(nums)
#         for L in range(n):
#             for R in range(L, n):
#                 if prod(nums[L:R+1]) < k: count += 1
#                 else: break
#         return count

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        left = 0
        count = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1
        return count