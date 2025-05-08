# from typing import List
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         count = 0
#         n = len(nums)
#         for i in range(n - 2):
#             for j in range(i + 1, n - 1):
#                 for k in range(j + 1, n):
#                     if nums[i] + nums[j] > nums[k]: count += 1
#                     else: break
#         return count

from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else: i += 1
        return count