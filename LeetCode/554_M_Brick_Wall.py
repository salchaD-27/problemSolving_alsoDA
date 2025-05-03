# from typing import List
# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         for i in range(len(wall)):
#             for j in range(1, len(wall[i])):
#                 wall[i][j]+=wall[i][j-1]
#         count=0
#         totalLen=sum(wall[0])
#         for i in range(totalLen):
#             tempCount=0
#             for j in range(len(wall)):
#                 if i in wall[j]: tempCount+=1
#             count=max(count,tempCount)
#         return len(wall)-count

from typing import List
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        for row in wall:
            prefix_sum = 0
            for brick in row[:-1]:  # except rightmost edge
                prefix_sum += brick
                edge_count[prefix_sum] += 1
        max_edges = max(edge_count.values(), default=0)
        return len(wall) - max_edges