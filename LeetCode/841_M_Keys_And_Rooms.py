# from typing import List
# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         locked=[i for i in range(1, len(rooms))]
#         queue=[0]
#         while queue:
#             currRoom=queue.pop(0)
#             keys=rooms[currRoom]
#             queue+=keys
#             for key in keys:
#                 if key in locked: locked.remove(key)
#         return not locked

from typing import List
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        locked = set(range(1, len(rooms)))
        queue = deque([0])
        while queue:
            currRoom = queue.popleft()
            for key in rooms[currRoom]:
                if key in locked:
                    locked.remove(key)
                    queue.append(key)
        return not locked