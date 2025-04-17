# from typing import List
# class Solution:
#     def numberOfBoomerangs(self, points: List[List[int]]) -> int:
#         points.sort()
#         count=0
#         for i in range(len(points)-1):
#             for j in range(i+1, len(points)):
#                 currXDiff=points[j][0]-points[i][0]
#                 currYDiff=points[j][1]-points[i][1]
#                 required=[points[j][0]+currXDiff,points[j][1]+currYDiff]
#                 if(required in points[j+1:]): count+=1
#         return 2*count
    
from typing import List
from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)):
            distance_map = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    # dist bw i-j
                    dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    distance_map[dist] += 1
            # if dist occurs one+, count boomrngs
            for dist in distance_map.values():
                count += dist * (dist - 1) # n*(n-1) boomrngs for each dist
        return count