# from typing import List
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         L,R,count=0,0,0
#         while L<len(nums):
#             if(sum(nums[L:R+1])==k):
#                 count+=1
#                 L+=1
#                 R=L
#             elif(sum(nums[L:R+1])<k): R+=1
#             elif(sum(nums[L:R+1])>k): 
#                 L+=1
#                 R=L
#         return count

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_map = {0: 1}
        count = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sum_map: count += prefix_sum_map[prefix_sum - k]
            if prefix_sum in prefix_sum_map: prefix_sum_map[prefix_sum] += 1
            else: prefix_sum_map[prefix_sum] = 1
        return count