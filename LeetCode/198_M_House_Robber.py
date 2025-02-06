# func rob(nums []int) int {
# 	odd:=0
#     even:=0
#     for i:=0; i<len(nums); i+=2 {odd+=nums[i]}
# 	for i:=1; i<len(nums); i+=2 {even+=nums[i]}
# 	if(odd>even){return odd
#     }else{return even}
# }

# from typing import List
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         ans=0
#         while(nums):
#             temp=0
#             tempI=0
#             for i in range(len(nums)):
#                 if(nums[i]>temp):
#                     temp=nums[i]
#                     tempI=i
#             ans+=temp
#             if(tempI==0): del nums[:tempI+2]
#             elif(tempI==len(nums)-1): del nums[tempI:]
#             else: del nums[tempI-1:tempI+2]
#         return ans

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums)==1: return nums[0]
        prev2, prev1 = 0, 0
        for num in nums:
            new_pick = max(prev1, prev2 + num)
            prev2, prev1 = prev1, new_pick
        return prev1