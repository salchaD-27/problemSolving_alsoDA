# from typing import List
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         def bigger(arr, val):
#             for num in arr:
#                 if num>val: return True
#             return False

#         first = second = nums[0]
#         for i in range(1, len(nums)):
#             if(first==second and nums[i]>second): second=nums[i]
#             elif(first!=second and nums[i]>second): return True
#             elif(first!=second and nums[i]<second):
#                 if(bigger(nums[i+1:], second)): continue
#                 else:
#                     first=second=nums[i]
#         if(first==second): return False
#         return False

from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first: first = num
            elif num <= second: second = num
            else: return True
        return False