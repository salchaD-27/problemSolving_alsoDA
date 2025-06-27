# from typing import List
# from collections import deque
# class Solution:
#     def shortestPathLength(self, graph: List[List[int]]) -> int:
#         nodesCount = len(graph)
#         queue = deque()
#         visited = set()
#         for i in range(nodesCount):
#             queue.append((str(i), 1 << i, i))
#         res = float('inf')
#         while queue:
#             currPath, pathMask, lastNode = queue.popleft()
#             if pathMask == (1 << nodesCount) - 1: return len(currPath) - 1
#             for nextNode in graph[lastNode]:
#                 if str(nextNode) not in currPath:
#                     nextPath = currPath + str(nextNode)
#                     nextMask = pathMask | (1 << nextNode)
#                     state = (nextPath, nextMask, nextNode)
#                     if state not in visited:
#                         visited.add(state)
#                         queue.append(state)
#         return res
    
from typing import List
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1: return 0
        queue = deque((i, 1 << i, 0) for i in range(n))  # node, visited, steps
        visited = set((i, 1 << i) for i in range(n))
        all_visited = (1 << n) - 1
        while queue:
            node, mask, dist = queue.popleft()
            for nei in graph[node]:
                next_mask = mask | (1 << nei)
                if next_mask == all_visited: return dist + 1
                if (nei, next_mask) not in visited:
                    visited.add((nei, next_mask))
                    queue.append((nei, next_mask, dist + 1))
        return -1