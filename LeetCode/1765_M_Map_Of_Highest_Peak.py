# from typing import List
# class Solution:
#     def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
#         rows, cols = len(isWater), len(isWater[0])        
#         for i in range(rows):
#             for j in range(cols):
#                 if isWater[i][j] == 0: isWater[i][j] =1
#                 elif isWater[i][j] == 1: isWater[i][j] = 0
#         for i in range(rows):
#             for j in range(cols):
#                 if isWater[i][j] != 0:
#                     neighbors = []
#                     if i > 0: neighbors.append(isWater[i-1][j])
#                     if i < rows - 1: neighbors.append(isWater[i+1][j])
#                     if j > 0: neighbors.append(isWater[i][j-1])
#                     if j < cols - 1: neighbors.append(isWater[i][j+1])
#                     isWater[i][j] = min(neighbors) + 1
#         for i in range(rows - 1, -1, -1):
#             for j in range(cols - 1, -1, -1):
#                 if isWater[i][j] != 0:
#                     neighbors = []
#                     if i > 0: neighbors.append(isWater[i-1][j])
#                     if i < rows - 1: neighbors.append(isWater[i+1][j])
#                     if j > 0: neighbors.append(isWater[i][j-1])
#                     if j < cols - 1: neighbors.append(isWater[i][j+1])
#                     isWater[i][j] = min(isWater[i][j], min(neighbors) + 1)
#         return isWater

from typing import List
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1 if isWater[i][j] == 0 else 0 for j in range(n)] for i in range(m)]
        
        from collections import deque
        queue = deque([(i, j) for i in range(m) for j in range(n) if isWater[i][j] == 1])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))
        return height