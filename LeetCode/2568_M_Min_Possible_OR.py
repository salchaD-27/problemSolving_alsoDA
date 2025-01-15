# from typing import List
# class Solution:
#     def minImpossibleOR(self, nums: List[int]) -> int:
#         expressible = set()
#         for num in nums:
#             new_values = set()
#             for val in expressible:
#                 new_values.add(val | num)
#             new_values.add(num)
#             expressible.update(new_values)
#         i = 1
#         while i in expressible:
#             i += 1
#         return i

from typing import List
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums_set = set(nums)
        x = 1 
        while x in nums_set:
            x *= 2 
        return x