# from typing import List
# from collections import Counter
# class Solution:
#     def triangleType(self, nums: List[int]) -> str:
#         def possTriangle(nums): return (nums[0]<nums[1]+nums[2]) and (nums[1]<nums[0]+nums[2]) and (nums[2]<nums[0]+nums[1])
#         count=Counter(nums)
#         if len(count)==1: return 'equilateral'
#         elif len(count)==2: return 'isosceles'
#         elif len(count)==3 and possTriangle(nums): return 'scalene'
#         else: return 'none'

from typing import List
from collections import Counter
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        def possTriangle(nums):  return nums[0] + nums[1] > nums[2]
        if not possTriangle(nums): return 'none'
        count = Counter(nums)
        if len(count) == 1: return 'equilateral'
        elif len(count) == 2: return 'isosceles'
        else: return 'scalene'