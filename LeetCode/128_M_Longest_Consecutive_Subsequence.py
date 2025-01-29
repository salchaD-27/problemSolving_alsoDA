# from typing import List
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if(nums==[]): return 0
#         start=min(nums)
#         count=0
#         while(True):
#             if(start in nums):
#                 count+=1
#                 start+=1
#             else: break
#         return count

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numSet = set(nums)
        max_length = 0
        for num in numSet:
            if num - 1 not in numSet:
                current_length = 1
                while num + 1 in numSet:
                    num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length