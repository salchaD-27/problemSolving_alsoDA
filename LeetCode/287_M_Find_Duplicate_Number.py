from typing import List
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = Counter(nums)
        for key, value in temp.items():
            if value > 1: return key
            
# from typing import List
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in range(len(nums)-1):
#             if(nums[i]==nums[i+1]): return nums[i]