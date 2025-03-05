# from typing import List
# class Solution:
#     def maxRotateFunction(self, nums: List[int]) -> int:
#         n = len(nums)
#         res = float('-inf')
#         for k in range(n):
#             temp = 0
#             for i in range(n):
#                 index = (i - k) % n
#                 temp += nums[index] * i
#             res = max(res, temp)
#         return res

from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        F_k = sum(i * num for i, num in enumerate(nums))
        max_F = F_k
        for k in range(1, n):
            F_k = F_k + total_sum - n * nums[-k]
            max_F = max(max_F, F_k)
        return max_F