from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def up(i, j, grid): 
            if i > 0: return [grid[i - 1][j], [i - 1, j]]
            return ["0", None]
        def down(i, j, grid): 
            if i < len(grid) - 1: return [grid[i + 1][j], [i + 1, j]]
            return ["0", None]
        def right(i, j, grid): 
            if j < len(grid[i]) - 1: return [grid[i][j + 1], [i, j + 1]]
            return ["0", None]
        def left(i, j, grid): 
            if j > 0: return [grid[i][j - 1], [i, j - 1]]
            return ["0", None]
        def connections(i, j, grid):
            visited.add((i, j))
            directions = [up(i, j, grid), down(i, j, grid), left(i, j, grid), right(i, j, grid)]
            for val, pos in directions:
                if pos and val == "1" and tuple(pos) not in visited: connections(pos[0], pos[1], grid)

        visited = set()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    ans += 1
                    connections(i, j, grid)
        return ans

# from typing import List
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(r, c):
#             if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or (r, c) in visited): return
#             visited.add((r, c))
#             dfs(r + 1, c)  # Down
#             dfs(r - 1, c)  # Up
#             dfs(r, c + 1)  # Right
#             dfs(r, c - 1)  # Left

#         if not grid: return 0
#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         islandCount = 0
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == '1' and (i, j) not in visited:
#                     islandCount += 1 
#                     dfs(i, j)
#         return islandCount