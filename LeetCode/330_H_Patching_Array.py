# from typing import List
# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:
#         def lastN(n):
#             ans=0
#             while(2**ans<n):
#                 ans+=1
#             return ans
#         return lastN(n)-len(nums)

# from typing import List
# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:
#         count=0
#         buffer=[i for i in range(1,n+1)]
#         for num in nums:
#             buffer.remove(num)
#         sumsNotAchieved=[i for i in range(1,n+1)]
#         L,R=0,0
#         while(L<len(nums)):
#             R=L
#             while(R<len(nums)):
#                 temp=sum(nums[L:R+1])
#                 if(temp in sumsNotAchieved): sumsNotAchieved.remove(temp)
#         if(not sumsNotAchieved): return count
#         while(sumsNotAchieved):
#             num=buffer.pop(0)
#             count+=1
#             nums.append(num)
#             nums.sort()
#             L,R=0,0
#             while(L<len(nums)):
#                 R=L
#                 while(R<len(nums)):
#                     temp=sum(nums[L:R+1])
#                     if(temp in sumsNotAchieved): sumsNotAchieved.remove(temp)
#         return count
    
from typing import List
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1
        i = 0 
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches