# from typing import List
# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         def heights(buildings, i):
#             res = []
#             for j in range(len(buildings)):
#                 if buildings[j][0] <= i < buildings[j][1]: res.append(buildings[j][2])
#             return res

#         res = [[buildings[0][0], buildings[0][2]]]
#         lastMaxHeight = buildings[0][2]
#         for i in range(buildings[0][0], buildings[-1][1] + 1):
#             temp = max(heights(buildings, i)) if heights(buildings, i) else 0
#             if temp != lastMaxHeight:
#                 lastMaxHeight = temp
#                 res.append([i, lastMaxHeight])
#         return res

from typing import List
import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height)) 
            events.append((right, height))
        events.sort() 
        res = []  
        max_heap = [0]
        prev_height = 0
        for x, h in events:
            if h < 0: heapq.heappush(max_heap, h)
            else:  
                max_heap.remove(-h)
                heapq.heapify(max_heap)
            cur_height = -max_heap[0]
            if cur_height != prev_height:
                res.append([x, cur_height])
                prev_height = cur_height
        return res