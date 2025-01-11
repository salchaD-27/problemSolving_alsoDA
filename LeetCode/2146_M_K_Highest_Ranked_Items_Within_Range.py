# from typing import List

# class Solution:
#     def dist(self, cell: List[int], start: List[int]) -> int: return abs(cell[0] - start[0]) + abs(cell[1] - start[1])
#     def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
#         res = []
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]>1 and pricing[0]<=grid[i][j]<=pricing[1]:
#                     res.append([self.dist([i, j], start), grid[i][j], i, j]) 
#         res.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
#         return [[item[2], item[3]] for item in res[:k]]

from typing import List
from collections import deque

class Solution:
    def dist(self, cell: List[int], start: List[int]) -> int: return abs(cell[0] - start[0]) + abs(cell[1] - start[1])
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        low, high = pricing
        start_row, start_col = start
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Initialing BFS queue and visiting set
        queue = deque([(start_row, start_col, 0)])
        visited = set([(start_row, start_col)])
        valid_items = []
        while queue:
            row, col, dist = queue.popleft()
            if low <= grid[row][col] <= high: valid_items.append((dist, grid[row][col], row, col))

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and grid[new_row][new_col] != 0):
                    queue.append((new_row, new_col, dist + 1))
                    visited.add((new_row, new_col))
        valid_items.sort()
        return [[row, col] for _, _, row, col in valid_items[:k]]