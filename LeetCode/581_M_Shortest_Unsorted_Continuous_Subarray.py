# from typing import List
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         if(len(nums)<2): return 0
#         startIdx=endIdx=-1
#         for i in range(1, len(nums)):
#             if(nums[i-1]>nums[i]): 
#                 startIdx=i-1
#                 break
#         for i in range(len(nums)-1,0,-1):
#             if(nums[i-1]>nums[i]): 
#                 endIdx=i
#                 break
#         return endIdx-startIdx+1 if endIdx!=startIdx!=-1 else 0

from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = -1, -2
        min_unsorted = float('inf')
        max_unsorted = float('-inf')
        for i in range(1, n):
            if nums[i] < nums[i - 1]: min_unsorted = min(min_unsorted, nums[i])
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]: max_unsorted = max(max_unsorted, nums[i])
        for l in range(n):
            if nums[l] > min_unsorted:
                start = l
                break
        for r in range(n - 1, -1, -1):
            if nums[r] < max_unsorted:
                end = r
                break
        return end - start + 1