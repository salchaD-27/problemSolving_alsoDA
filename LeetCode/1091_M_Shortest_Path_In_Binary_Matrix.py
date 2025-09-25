from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Step 1: Handle impossible start/end cases
        if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1
        # Special case: single cell grid and it's open
        if n == 1: return 1
        # Step 2: All 8 directions (rowChange, colChange)
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
        # Step 3: BFS setup
        q = deque()
        visited = [[False] * n for _ in range(n)]
        # Start BFS from (0,0) with 1 step
        q.append((0, 0, 1))
        visited[0][0] = True
        # Step 4: BFS loop
        while q:
            r, c, dist = q.popleft()
            # If we reached destination
            if r == n - 1 and c == n - 1: return dist
            # Try all directions
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
        # Step 5: No path exists
        return -1