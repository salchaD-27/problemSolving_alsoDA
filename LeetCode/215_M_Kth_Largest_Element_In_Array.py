# from typing import List
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         largest=[nums[0]]
#         minInLargest=min(largest)
#         for i in range(len(nums)):
#             if(nums[i]>minInLargest and len(largest)<k): largest.append(nums[i])
#             elif(nums[i]>minInLargest and len(largest)==k):
#                 largest.pop(-1)
#                 largest.append(nums[i])
#             largest.sort(reverse=True)
#             minInLargest=min(largest)
#         return largest[-1]
    
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val, max_val = min(nums), max(nums)
        count = [0] * (max_val - min_val + 1)
        for num in nums:
            count[num - min_val] += 1
        remaining = k
        for i in range(len(count) - 1, -1, -1):
            remaining -= count[i]
            if remaining <= 0: return i + min_val