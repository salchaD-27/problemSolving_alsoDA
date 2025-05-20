# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#         # 1oc, 2oc, 4oc, 5oc, 7oc, 8oc, 10oc, 11oc
#         dirs=[[-2,1],[-1,2],[1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]
#         possMoves=[0]*k
#         def possOnBoardMoves(row, col, k):
#             if k>0:
#                 poss=0
#                 for i in range(len(dirs)):
#                     newRow=row+dirs[i][0]
#                     newCol=col+dirs[i][1]
#                     if 0<=newRow<n and 0<=newCol<n: 
#                         poss+=1
#                         possOnBoardMoves(newRow, newCol, k-1)
#                 possMoves[k-1]+=poss
#             else: return
        
#         possOnBoardMoves(row, column, k)
#         prob,eightMul=1,1
#         for i in reversed(range(len(possMoves))):
#             prob*=possMoves[i]/(8*eightMul)
#             eightMul+=1
#         return prob

from functools import lru_cache
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        
        @lru_cache(maxsize=None)
        def dfs(r, c, moves_left):
            if r < 0 or r >= n or c < 0 or c >= n: return 0.0
            if moves_left == 0: return 1.0
            prob = 0.0
            for dr, dc in directions:
                prob += dfs(r + dr, c + dc, moves_left - 1) / 8
            return prob
        return dfs(row, column, k)