# from typing import List
# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         res = []

#         def traverseSouthWest(start):
#             x, y = start
#             while 0 <= x < len(mat) and 0 <= y < len(mat[0]):
#                 res.append(mat[x][y])
#                 x += 1
#                 y -= 1
#             traverseNorthEast([x, y])
#         def traverseNorthEast(start):
#             x, y = start
#             while 0 <= x < len(mat) and 0 <= y < len(mat[0]):
#                 res.append(mat[x][y])
#                 x -= 1
#                 y += 1
#             traverseSouthWest([x, y])
#         traverseNorthEast([0, 0])
#         return res

from typing import List
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        N, M = len(matrix), len(matrix[0])
        result, intermediate = [], []
        for d in range(N + M - 1):
            intermediate.clear()
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            if d % 2 == 0: result.extend(intermediate[::-1])
            else: result.extend(intermediate)
        return result