# from typing import List
# class Solution:
#     def flipgame(self, fronts: List[int], backs: List[int]) -> int:
#         origFronts,origBacks=fronts,backs
#         nums=list(set(fronts+backs))
#         nums.sort()
#         notPoss=[]
#         for i in range(len(fronts)):
#             if fronts[i]==backs[i]: notPoss.append(fronts[i])
#         for i in range(len(nums)):
#             if nums[i] in notPoss:
#                 fronts,backs=origBacks,origBacks
#                 for i in range(len(fronts)):
#                     if fronts[i]==nums[i]: fronts[i],backs[i]=backs[i],fronts[i]
#                 if nums[i] not in fronts: return nums[i]
#         return 0

from typing import List
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        origFronts, origBacks = fronts, backs
        nums = sorted(set(fronts + backs))
        notPoss = []
        for i in range(len(fronts)):
            if fronts[i] == backs[i]: notPoss.append(fronts[i])
        for num in nums:
            if num not in notPoss: return num
        return 0
    
from typing import List
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        candidates = [x for x in fronts + backs if x not in same]
        return min(candidates) if candidates else 0