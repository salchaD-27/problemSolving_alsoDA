# from typing import List
# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         def subSolver(nums, pivot, index):
#             res=[pivot]
#             for i in range(index+1, len(nums)):
#                 if(nums[i]%res[-1]==0): res.append(nums[i])
#             return res
        
#         if(len(nums)<2): return nums
#         nums.sort()
#         for i in range(len(nums)):
#             res=subSolver(nums, nums[i], i)
#             if(len(res)>1): return res

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_size = 0
        max_index = -1
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        return result[::-1]