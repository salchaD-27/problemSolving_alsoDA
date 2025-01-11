# from typing import List
# class Solution:
#     def aptSum(self, n: int) -> int:
#         sum = 0
#         for i in range(1, n + 1):
#             sum += 2**(i - 1)
#         return sum
#     def numberOfWeeks(self, milestones: List[int]) -> int: return min(sum(milestones), self.aptSum(len(milestones))) 

from typing import List
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        if max(milestones) > sum(milestones) - max(milestones): return 2 * (sum(milestones) - max(milestones)) + 1 
        return sum(milestones)