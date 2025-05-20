# from typing import List
# class Solution:
#     def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
#         references=[0]*len(nums)
#         for i in range(len(queries)):
#             startIdx, endIdx=queries[i][0], queries[i][1]
#             for idx in range(startIdx, endIdx+1):
#                 references[idx]+=1
#         for i in range(len(nums)):
#             if references[i]<nums[i]: return False
#         return True
    
class Solution(object):
    def isZeroArray(self, nums, queries):
        diff = [0]*(len(nums) + 1)
        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(nums): diff[r + 1] -= 1
        cnt = 0
        for i in range(len(nums)):
            cnt += diff[i]
            if nums[i] > cnt: return False
        return True