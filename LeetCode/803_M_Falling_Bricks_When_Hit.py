from typing import List
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        parent = {}
        size = {}
        top = m * n

        def index(x, y): return x * n + y
        def find(x):
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY: return
            parent[rootX] = rootY
            size[rootY] += size[rootX]
        def is_connected_to_top(x, y): return find(index(x, y)) == find(top)

        grid_copy = [row[:] for row in grid]
        for x, y in hits:
            grid_copy[x][y] = 0
        for i in range(m):
            for j in range(n):
                if grid_copy[i][j] == 1:
                    idx = index(i, j)
                    parent[idx] = idx
                    size[idx] = 1
        parent[top] = top
        size[top] = 1

        def add_brick(x, y):
            if grid_copy[x][y] != 1: return
            idx = index(x, y)
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid_copy[nx][ny] == 1: union(idx, index(nx, ny))
            if x == 0: union(idx, top)

        for i in range(m):
            for j in range(n):
                if grid_copy[i][j] == 1: add_brick(i, j)
        res = []
        for x, y in reversed(hits):
            before = size[find(top)]
            if grid[x][y] == 0:
                res.append(0)
                continue
            grid_copy[x][y] = 1
            idx = index(x, y)
            parent[idx] = idx
            size[idx] = 1
            add_brick(x, y)
            after = size[find(top)]
            fallen = max(0, after - before - 1)
            res.append(fallen)
        return res[::-1]
    
from typing import List
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        grid_copy = [row[:] for row in grid]
        for x, y in hits:
            grid_copy[x][y] -= 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid_copy[i][j] != 1: return 0
            grid_copy[i][j] = 2
            count = 1
            for dx, dy in directions:
                count += dfs(i + dx, j + dy)
            return count

        for j in range(cols):
            dfs(0, j)
        res = [0] * len(hits)
        for k in reversed(range(len(hits))):
            x, y = hits[k]
            grid_copy[x][y] += 1
            if grid_copy[x][y] != 1: continue
            
            def is_stable(i, j):
                if i == 0: return True
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols and grid_copy[ni][nj] == 2: return True
                return False
            
            if is_stable(x, y):
                fallen = dfs(x, y) - 1
                res[k] = fallen
        return res