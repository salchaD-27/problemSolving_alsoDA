# from typing import List
# class Solution:
#     def arrayNesting(self, nums: List[int]) -> int:
#         res=0
#         for i in range(len(nums)):
#             lastAdded=nums[i]
#             temp=1
#             while(True):
#                 nextAdded=nums[lastAdded]
#                 if(nextAdded==lastAdded): break
#                 else:
#                     lastAdded=nextAdded
#                     temp+=1
#             res=max(res,temp)
#         return res

from typing import List
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                count = 0
                current = i
                while not visited[current]:
                    visited[current] = True
                    current = nums[current]
                    count += 1
                res = max(res, count)
        return res