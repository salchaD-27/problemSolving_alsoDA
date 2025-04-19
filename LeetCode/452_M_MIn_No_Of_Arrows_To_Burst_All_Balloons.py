# [1,6]
# [2,8]
#     [2,6]
# [7,12]
# [10,16]
#     [10,12]

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[0])
        newPoints = []
        newPoints.append(points[0])
        for i in range(1, len(points)):
            if points[i][0] > newPoints[-1][1]: newPoints.append(points[i])
            else: newPoints[-1] = [newPoints[-1][0], min(newPoints[-1][1], points[i][1])]
        return len(newPoints)
    
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        current_end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > current_end:
                arrows += 1
                current_end = points[i][1]
        return arrows