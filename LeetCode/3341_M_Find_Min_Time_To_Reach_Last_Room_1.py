# from typing import List
# class Solution:
#     def minTimeToReach(self, moveTime: List[List[int]]) -> int:
#         temp=moveTime[-1][-1]
#         for i in range(1, len(moveTime[0])):
#             moveTime[0][i]+=1+moveTime[0][i-1]
#         for i in range(1, len(moveTime)):
#             moveTime[i][0]+=1+moveTime[i-1][0]
#         for i in range(1,len(moveTime)):
#             for j in range(1, len(moveTime[i])):
#                 moveTime[i][j]+=1+min(moveTime[i-1][j],moveTime[i][j-1])
#         return moveTime[-1][-1]-temp

import heapq
class State:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis
    def __lt__(self, other):
        return self.dis < other.dis
class Solution:
    def minTimeToReach(self, moveTime):
        n = len(moveTime)
        m = len(moveTime[0])
        inf = float("inf")
        d = [[inf] * m for _ in range(n)]
        v = [[0] * m for _ in range(n)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        d[0][0] = 0
        q = []
        heapq.heappush(q, State(0, 0, 0))
        while q:
            s = heapq.heappop(q)
            if v[s.x][s.y]: continue
            v[s.x][s.y] = 1
            for dx, dy in dirs:
                nx, ny = s.x + dx, s.y + dy
                if not (0 <= nx < n and 0 <= ny < m): continue
                dist = max(d[s.x][s.y], moveTime[nx][ny]) + 1
                if d[nx][ny] > dist:
                    d[nx][ny] = dist
                    heapq.heappush(q, State(nx, ny, dist))
        return d[n - 1][m - 1]