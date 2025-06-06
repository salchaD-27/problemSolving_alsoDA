# from typing import List
# class Solution:
#     def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
#         def all1(i, j, dir, count):
#             if dir=='L':
#                 for k in range(j, j-count-1, -1):
#                     if [i, k] in mines: return False
#                 return True
#             if dir=='R':
#                 for k in range(j, j+count+1):
#                     if [i, k] in mines: return False
#                 return True
#             if dir=='U':
#                 for k in range(i, i-count-1, -1):
#                     if [k, j] in mines: return False
#                 return True
#             if dir=='D':
#                 for k in range(i, i+count+1):
#                     if [k, j] in mines: return False
#                 return True

#         k=0
#         for i in range(n):
#             for j in range(n):
#                 left, right, up, down=j-0, n-1-j, i-0, n-1-i
#                 tempK=min(left,right,up,down)+1
#                 if tempK>k and [i,j] not in mines:
#                     if tempK==1: k=1
#                     else:
#                         if all1(i, j, 'L', left) and all1(i, j, 'R', right) and all1(i, j, 'U', up) and all1(i, j, 'D', down): k=tempK
#         return k

from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[n] * n for _ in range(n)]
        banned = set(tuple(mine) for mine in mines)
        for i in range(n):
            count = 0
            # Left
            for j in range(n):
                if (i, j) in banned: count = 0
                else: count += 1
                grid[i][j] = min(grid[i][j], count)
            count = 0
            # Right
            for j in reversed(range(n)):
                if (i, j) in banned: count = 0
                else: count += 1
                grid[i][j] = min(grid[i][j], count)
        for j in range(n):
            count = 0
            # Up
            for i in range(n):
                if (i, j) in banned: count = 0
                else: count += 1
                grid[i][j] = min(grid[i][j], count)
            count = 0
            # Down
            for i in reversed(range(n)):
                if (i, j) in banned: count = 0
                else: count += 1
                grid[i][j] = min(grid[i][j], count)
        return max(max(row) for row in grid)