# import math
# from typing import List
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         if h == len(piles): return max(piles)
#         k = 1
#         while True:
#             tmp = 0
#             for pile in piles:
#                 tmp += math.ceil(pile / k)
#                 if tmp > h: break
#             if tmp <= h: return k
#             k += 1

import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            total = sum(math.ceil(pile / mid) for pile in piles)
            if total > h: left = mid + 1
            else: right = mid
        return left