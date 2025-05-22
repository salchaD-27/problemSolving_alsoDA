# from typing import List
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         dp=[0 for _ in range(len(grid[0]))]*len(grid)
#         for i in range(1, len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j]==1: dp[i][j]=1
#                 if j==0 and grid[i-1][j]==1: dp[i][j]=1+dp[i-1][j]
#                 else:
#                     if grid[i-1][j]==1: dp[i][j]+=dp[i-1][j]
#                     if grid[i][j-1]==1: dp[i][j]+=dp[i][j-1]
#         area=0
#         for i in range(len(dp)):
#             for j in range(len(dp[i])):
#                 area=max(area, dp[i][j])
#         return area

from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def get_area(i, j):
            stack = [(i, j)]
            area = 0
            while stack:
                r, c = stack.pop()
                if (0 <= r < rows and 0 <= c < cols 
                    and grid[r][c] == 1 and not visited[r][c]):
                    visited[r][c] = True
                    area += 1
                    stack.append((r+1, c))
                    stack.append((r-1, c))
                    stack.append((r, c+1))
                    stack.append((r, c-1))
            return area
        
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]: max_area = max(max_area, get_area(i, j))
        return max_area