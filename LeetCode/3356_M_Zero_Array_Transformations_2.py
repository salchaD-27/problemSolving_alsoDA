# from typing import List
# class Solution:
#     def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
#         def isPossible(k):
#             n = len(nums)
#             temp = nums[:]
#             diff = [0] * (n + 1) 
#             for i in range(k):
#                 li, ri, vali = queries[i]
#                 diff[li] -= vali
#                 diff[ri + 1] += vali
#             curr_decrement = 0
#             for i in range(n):
#                 curr_decrement += diff[i]
#                 temp[i] += curr_decrement 
#                 temp[i] = max(0, temp[i]) 
#             return all(x == 0 for x in temp)

#         left, right = 1, len(queries)
#         answer = -1        
#         while left <= right:
#             mid = (left + right) // 2
#             if isPossible(mid):
#                 answer = mid 
#                 right = mid - 1
#             else: left = mid + 1
#         return answer

from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isPossible(k):
            n = len(nums)
            temp = nums[:]
            diff = [0] * (n + 1)
            for i in range(k):
                li, ri, vali = queries[i]
                diff[li] -= vali
                diff[ri + 1] += vali
            curr_decrement = 0
            for i in range(n):
                curr_decrement += diff[i]
                temp[i] += curr_decrement
                temp[i] = max(0, temp[i])
            return all(x == 0 for x in temp)
        
        if all(x == 0 for x in nums): return 0
        left, right = 1, len(queries)
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if isPossible(mid):
                answer = mid 
                right = mid - 1
            else: left = mid + 1
        return answer