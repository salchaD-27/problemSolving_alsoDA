# from typing import List
# class Solution:
#     def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
#         rowMap = {}
#         for i in range(len(mat)):
#             rowMap[i] = len(mat[i]) 
#         colMap = {}
#         for j in range(len(mat[0])):
#             colMap[j] = len(mat)    
#         elemMap = {}
#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 elemMap[mat[i][j]] = [i, j]
#         for i in range(len(arr)):
#             row, col = elemMap[arr[i]]
#             rowMap[row] -= 1
#             colMap[col] -= 1
#             if rowMap[row] == 0 or colMap[col] == 0: return i
#         return -1

from typing import List
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rowCount = [n] * m          
        colCount = [m] * n          
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        for i, val in enumerate(arr):
            row, col = position[val]
            rowCount[row] -= 1
            colCount[col] -= 1
            if rowCount[row] == 0 or colCount[col] == 0: return i
        return -1