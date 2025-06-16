# from typing import List
# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
#         def maxOfCol(col):
#             val=0
#             for i in range(len(grid)):
#                 val=max(val, grid[i][col])
#             return val

#         heights=[[0]*len(grid[0])]*len(grid)
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 heights[i][j]=maxOfCol(j)-grid[i][j]
#         res=0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 heights[i][j]=min(heights[i][j], max(grid[i])-grid[i][j])
#                 res+=heights[i][j]
#         return res

from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]
        res = 0
        for i in range(n):
            for j in range(n):
                allowed_height = min(row_max[i], col_max[j])
                res += allowed_height - grid[i][j]
        return res