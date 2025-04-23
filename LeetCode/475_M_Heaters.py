# 1 2 3 4
# 0 1 1 0

# from typing import List
# class Solution:
#     def findRadius(self, houses: List[int], heaters: List[int]) -> int:
#         dp=[0]*len(houses)
#         for i in range(len(dp)):
#             dp[i]=min(abs(houses[i]-heaters[j]) for j in range(len(heaters)))
#         return max(dp)

import bisect
from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            left = abs(house - heaters[idx - 1]) if idx > 0 else float('inf')
            right = abs(house - heaters[idx]) if idx < len(heaters) else float('inf')
            closest = min(left, right)
            radius = max(radius, closest)
        return radius