# from typing import List
# class Solution:
#     def isSelfCrossing(self, distance: List[int]) -> bool:
#         if(len(distance)<4): return False
#         x,y,s=0,0,1
#         #     North, West, South, East
#         iter=[[0,1],[-1,0],[0,-1],[1,0]]
#         for i in range(0,3):
#             x,y+=distance[i]*(iter[i%4])
#             if(y<0): s=-1
#             else: s=1
#         for i in range(3,len(distance)):

from typing import List
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        if n < 4: return False
        for i in range(3, n):
            # 4th step crosses first
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]: return True
            # 5th step crosses first (overlapping case)
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]: return True
            # 6th step crosses first (loop case)
            if ((i >= 5)
                and (distance[i-2] >= distance[i-4])
                and (distance[i] >= distance[i-2] - distance[i-4])
                and (distance[i-1] <= distance[i-3])
                and (distance[i-1] >= distance[i-3] - distance[i-5])): return True
        return False