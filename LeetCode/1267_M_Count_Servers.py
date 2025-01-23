# from typing import List
# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         visited=[]
#         count=0
#         # Row
#         for i in range(len(grid)):
#             for j in range(len(grid[i])-1):
#                 if(grid[i][j]==1 and grid[i][j+1]==1):
#                     if([i,j] not in visited):
#                         count+=1
#                         visited.append([i,j])
#                     if([i,j+1] not in visited):
#                         count+=1
#                         visited.append([i,j+1])
#         # Cols
#         for i in range(len(grid)):
#             for j in range(len(grid[i])-1):
#                 if(grid[j][i]==1 and grid[j][i+1]==1):
#                     if([j,i] not in visited):
#                         count+=1
#                         visited.append([j,i])
#                     if([j,i+1] not in visited):
#                         count+=1
#                         visited.append([j,i+1])
#         return count

from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_count = [0] * m
        col_count = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    count += 1
        return count