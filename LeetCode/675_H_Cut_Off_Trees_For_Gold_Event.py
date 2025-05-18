# from typing import List
# class Solution:
#     def cutOffTree(self, forest: List[List[int]]) -> int:
#         rows, cols = len(forest), len(forest[0])
#         visited = [[False for _ in range(cols)] for _ in range(rows)]

#         def getMinValidDirection(i, j):
#             visited[i][j] = True
#             min_val = float('inf')
#             direction = [0, 0]
#             for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 ni, nj = i + di, j + dj
#                 if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj] and forest[ni][nj] != 0:
#                     if forest[ni][nj] < min_val:
#                         min_val = forest[ni][nj]
#                         direction = [di, dj]
#             if min_val == float('inf'): return False, [0, 0]
#             return True, direction

#         treesToCut = 0
#         for i in range(rows):
#             for j in range(cols):
#                 if forest[i][j] > 1: treesToCut += 1
#         i, j, steps = 0, 0, 0
#         while treesToCut:
#             poss, dir = getMinValidDirection(i, j)
#             if not poss: return -1
#             i += dir[0]
#             j += dir[1]
#             steps += 1
#             if forest[i][j] > 1:
#                 forest[i][j] = 1
#                 treesToCut -= 1
#         return steps

from typing import List
from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        rows, cols = len(forest), len(forest[0])

        def findPath(sr, sc, tr, tc):
            if sr == tr and sc == tc: return 0
            visited = [[False]*cols for _ in range(rows)]
            q = deque([(sr, sc, 0)])
            visited[sr][sc] = True
            while q:
                r, c, steps = q.popleft()
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc: return steps + 1
                        visited[nr][nc] = True
                        q.append((nr, nc, steps + 1))
            return -1

        trees = []
        for i in range(rows):
            for j in range(cols):
                if forest[i][j] > 1: trees.append((forest[i][j], i, j))
        trees.sort()
        i, j, total_steps = 0, 0, 0
        for height, ti, tj in trees:
            steps = findPath(i, j, ti, tj)
            if steps == -1: return -1
            total_steps += steps
            i, j = ti, tj
        return total_steps