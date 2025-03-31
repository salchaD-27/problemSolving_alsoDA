# from typing import List
# class Solution:
#     def putMarbles(self, weights: List[int], k: int) -> int:
#         maxS=0
#         minS=sum(weights)
#         for i in range(1, len(weights)-1):
#             bag1=weights[:i]
#             bag2=weights[i:]
#             score=bag1[0]+bag1[-1]+bag2[0]+bag2[-1]
#             maxS=max(maxS, score)
#             minS=min(minS, score)
#         return maxS-minS
    
from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        pair_sums = []
        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i + 1])
        pair_sums.sort()
        max_score = sum(pair_sums[-(k-1):])
        min_score = sum(pair_sums[:(k-1)])
        return max_score - min_score