# from typing import List
# class Solution:
#     def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
#         count=0
#         opened=[]
#         queue=initialBoxes
#         while queue:
#             box=queue.pop(0)
#             if box not in opened and status[box]==1:
#                 opened.append(box)
#                 count+=candies[box]
#                 for cbox in containedBoxes[box]:
#                     status[cbox]=1
#                     queue.append(cbox)
#         return count

# from typing import List
# from collections import deque
# class Solution:
#     def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
#         queue = deque(initialBoxes)
#         haveBoxes = set(initialBoxes)
#         haveKeys = set(i for i, s in enumerate(status) if s == 1)
#         visited = set()
#         totalCandies = 0
#         while queue:
#             box = queue.popleft()
#             if box in visited: continue
#             if status[box] == 1 or box in haveKeys:
#                 visited.add(box)
#                 totalCandies += candies[box]
#                 for key in keys[box]:
#                     if key not in haveKeys:
#                         haveKeys.add(key)
#                         if key in haveBoxes and key not in visited: queue.append(key)
#                 for newBox in containedBoxes[box]:
#                     if newBox not in haveBoxes:
#                         haveBoxes.add(newBox)
#                         queue.append(newBox)
#                     elif newBox in haveKeys and newBox not in visited: queue.append(newBox)
#             else: queue.append(box)
#         return totalCandies

from typing import List
from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(initialBoxes)
        haveBoxes = set(initialBoxes)
        haveKeys = set(i for i, s in enumerate(status) if s == 1)
        visited = set()
        waiting = set()
        totalCandies = 0
        while queue:
            box = queue.popleft()
            if box in visited: continue
            if status[box] == 1 or box in haveKeys:
                visited.add(box)
                totalCandies += candies[box]
                for key in keys[box]:
                    if key not in haveKeys:
                        haveKeys.add(key)
                        if key in waiting: queue.append(key)
                for newBox in containedBoxes[box]:
                    haveBoxes.add(newBox)
                    if status[newBox] == 1 or newBox in haveKeys: queue.append(newBox)
                    else: waiting.add(newBox)
            else: waiting.add(box)
        return totalCandies