# from typing import List
# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         def islands(grid):
#             def dfs(i, j):
#                 stack = [(i, j)]
#                 visited.add((i, j))
#                 size = 0
#                 while stack:
#                     x, y = stack.pop()
#                     size += 1
#                     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                         ni, nj = x + dx, y + dy
#                         if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1 and (ni, nj) not in visited:
#                             visited.add((ni, nj))
#                             stack.append((ni, nj))
#                 return size
            
#             visited = set()
#             maxSize = 0
#             for i in range(len(grid)):
#                 for j in range(len(grid[i])):
#                     if grid[i][j] == 1 and (i, j) not in visited: maxSize = max(maxSize, dfs(i, j))
#             return maxSize

#         maxIsland = islands(grid)
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == 0:
#                     grid[i][j] = 1 
#                     maxIsland = max(maxIsland, islands(grid))
#                     grid[i][j] = 0 
#         return maxIsland

from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y, id):
            stack = [(x, y)]
            grid[x][y] = id
            size = 0
            while stack:
                i, j = stack.pop()
                size += 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = id
                        stack.append((ni, nj))
            return size
        
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island_id = 2  
        island_sizes = {0: 0} 
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1
        max_island = max(island_sizes.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    possible_size = 1 
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1: seen.add(grid[ni][nj]) 
                    for island in seen:
                        possible_size += island_sizes[island] 
                    max_island = max(max_island, possible_size)
        return max_island