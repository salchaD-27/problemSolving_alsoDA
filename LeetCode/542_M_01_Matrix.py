# from typing import List
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 if(mat[i][j]==1):
#                     # if top left
#                     if(i==0 and j==0): mat[i][j]=1+min(mat[i+1][j],mat[i][j+1])
#                     # if top right
#                     elif(i==0 and j==len(mat[i])-1): mat[i][j]=1+min(mat[i][j-1],mat[i+1][j])
#                     # if bottom left
#                     elif(i==len(mat)-1 and j==0): mat[i][j]=1+min(mat[i-1][j],mat[i][j+1])
#                     # if bottom right
#                     elif(i==len(mat)-1 and j==len(mat[i])-1): mat[i][j]=1+min(mat[i-1][j],mat[i][j-1])
#                     # if in top row
#                     elif(i==0): mat[i][j]=1+min(mat[i][j-1],mat[i+1][j],mat[i][j+1])
#                     # if in bottom row
#                     elif(i==len(mat)-1): mat[i][j]=1+min(mat[i-1][j],mat[i][j-1],mat[i][j+1])
#                     # if in first col
#                     elif(j==0): mat[i][j]=1+min(mat[i-1][j],mat[i+1][j],mat[i][j+1])
#                     # if in last col
#                     elif(j==len(mat[i])-1): mat[i][j]=1+min(mat[i-1][j],mat[i][j-1],mat[i+1][j])
#                     # else... mid
#                     else: mat[i][j]=1+min(mat[i-1][j],mat[i][j-1],mat[i+1][j],mat[i][j+1])
#         return mat

from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0: dist[i][j] = 0
                else:
                    if i > 0: dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if j > 0: dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i < rows - 1: dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < cols - 1: dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        return dist