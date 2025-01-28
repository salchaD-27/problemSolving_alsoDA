from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def nexts(grid, i, j):
            neighbors = []
            rows, cols = len(grid), len(grid[0])
            # Top
            if i > 0: neighbors.append([grid[i-1][j], i-1, j])
            # Bottom
            if i < rows - 1: neighbors.append([grid[i+1][j], i+1, j])
            # Left
            if j > 0: neighbors.append([grid[i][j-1], i, j-1])
            # Right
            if j < cols - 1: neighbors.append([grid[i][j+1], i, j+1])
            return neighbors
        def subMaxFish(grid, i, j):
            stack = [(i, j)]
            visited.add((i, j))
            fish = 0
            while stack:
                x, y = stack.pop()
                fish += grid[x][y]
                for _, nx, ny in nexts(grid, x, y):
                    if (nx, ny) not in visited and grid[nx][ny] > 0:
                        stack.append((nx, ny))
                        visited.add((nx, ny))
            return fish

        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] > 0: ans = max(ans, subMaxFish(grid, i, j))
        return ans