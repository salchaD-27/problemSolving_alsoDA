# from typing import List
# class Solution:
#     def fallingSquares(self, positions: List[List[int]]) -> List[int]:
#         landingIntervals=[[positions[0][0], positions[0][0]+positions[0][1]]]
#         height=positions[0][1]
#         for i in range(len(positions)):
#             newInterval=True
#             for j in range(len(landingIntervals)):
#                 if landingIntervals[j][0]<=positions[i][0]<landingIntervals[j][1]:
#                     landingIntervals[j][1]=max(landingIntervals[j][1],positions[i][0]+positions[i][1])
#                     height=max(height,)
#                     newInterval=False
#             if newInterval: landingIntervals.append([positions[i][0],positions[i][0]+positions[i][1]])

from typing import List
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        result = []
        intervals = []
        max_height = 0
        for left, size in positions:
            right = left + size
            base_height = 0
            for l, r, h in intervals:
                if not (r <= left or l >= right): base_height = max(base_height, h)
            new_height = base_height + size
            intervals.append((left, right, new_height))
            max_height = max(max_height, new_height)
            result.append(max_height)
        return result