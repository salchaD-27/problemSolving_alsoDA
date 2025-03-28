# from collections import deque
# from typing import List
# class Solution:
#     def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
#         m, n = len(grid), len(grid[0])
#         k = len(queries)
#         answer = []
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         for query in queries:
#             visited = set() 
#             points = 0
#             queue = deque([(0, 0)])  
#             while queue:
#                 i, j = queue.popleft()
#                 if grid[i][j] < query and (i, j) not in visited:
#                     visited.add((i, j)) 
#                     points += 1 
#                 if grid[i][j] < query:
#                     for di, dj in directions:
#                         ni, nj = i + di, j + dj
#                         if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited: queue.append((ni, nj))
#             answer.append(points)
#         return answer

from typing import List
from heapq import heappop, heappush
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        q = [(n, i) for i, n in enumerate(queries)]
        q.sort() 
        min_heap = [(grid[0][0], 0, 0)] 
        res = [0] * len(queries)
        visit = set()
        visit.add((0, 0))
        points = 0
        for limit, index in q:
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heappop(min_heap)
                points += 1  
                neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for nr, nc in neighbors:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visit.add((nr, nc))
            res[index] = points
        return res