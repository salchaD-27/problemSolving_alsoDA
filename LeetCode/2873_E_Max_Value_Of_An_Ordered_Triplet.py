# from typing import List
# class Solution:
#     def maximumTripletValue(self, nums: List[int]) -> int:
#         I=0
#         Iidx=0
#         for i in range(len(nums)-2):
#             if(nums[i]>I):
#                 I=nums[i]
#                 Iidx=i
#         J=max(nums)
#         Jidx=0
#         for j in range(Iidx, len(nums)-1):
#             if(nums[j]<J):
#                 J=nums[j]
#                 Jidx=j
#         K=0
#         Kidx=0
#         for k in range(Jidx, len(nums)):
#             if(nums[k]>K):
#                 K=nums[k]
#                 Kidx=k
#         return max(0, (I-J)*K)
    
from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        left = nums[0]
        for j in range(1, N):
            if nums[j] > left:
                left = nums [j]
                continue
            for k in range(j + 1, N):
                res = max(res, (left - nums [j]) * nums [k])
        return res