# from typing import List
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if(sum(nums)<target): return 0
#         if(target in nums): return 1
#         if(sum(nums)==target): return len(nums)
#         ans=float('inf')
#         for i in range(len(nums)-1):
#             for j in range(i, len(nums)):
#                 if(sum(nums[i:j+1])==target): 
#                     temp=j-i+1
#                     if(temp<ans): ans=temp
#         return ans
    
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        ans = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0