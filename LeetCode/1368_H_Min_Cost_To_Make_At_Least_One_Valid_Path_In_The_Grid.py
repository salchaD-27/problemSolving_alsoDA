from typing import List
from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRS = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        visited = [[False]*n for _ in range(m)]
        dq = deque()
        dq.append((0, 0, 0))
        while dq:
            x, y, cost = dq.popleft()
            if visited[x][y]: continue
            visited[x][y] = True
            if x == m - 1 and y == n - 1: return cost
            for d in range(1, 5):
                dx, dy = DIRS[d]
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if d == grid[x][y]: dq.appendleft((nx, ny, cost))
                    else: dq.append((nx, ny, cost + 1))
        return -1