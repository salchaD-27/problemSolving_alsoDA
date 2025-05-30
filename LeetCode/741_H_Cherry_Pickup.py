# from typing import List
# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         dp=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
#         for i in range(len(grid)-1, -1, -1):
#             for j in range(len(grid[i])-1, -1, -1):
#                 # last cell
#                 if i==len(grid)-1 and j==len(grid[i])-1: dp[i][j]=1 if grid[i][j]==1 else 0
#                 # last row
#                 elif i==len(grid)-1: 
#                     if grid[i][j]==-1: dp[i][j]=0
#                     else: dp[i][j]=1+dp[i][j+1] if grid[i][j]==1 else dp[i][j+1]
#                 # last col
#                 elif j==len(grid[i])-1: 
#                     if grid[i][j]==-1: dp[i][j]=0
#                     else: dp[i][j]=1+dp[i+1][j] if grid[i][j]==1 else dp[i+1][j]
#                 else:
#                     if grid[i][j]==-1: dp[i][j]=0
#                     elif grid[i][j]==1: dp[i][j]=1+max(dp[i+1][j], dp[i][j+1])
#                     else: dp[i][j]=max(dp[i+1][j], dp[i][j+1])
#         downScore=dp[0][0]

from typing import List
from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        @lru_cache(None)
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n: return -float('inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1: return -float('inf')
            if r1 == c1 == r2 == c2 == n - 1: return grid[r1][c1]
            result = grid[r1][c1]
            if r1 != r2 or c1 != c2: result += grid[r2][c2]
            result += max(
                dp(r1 + 1, c1, r2 + 1),   # both move down
                dp(r1, c1 + 1, r2),       # right-down
                dp(r1 + 1, c1, r2),       # down-right
                dp(r1, c1 + 1, r2 + 1)    # both move right
            )
            return result
        ans = dp(0, 0, 0)
        return max(ans, 0) #type: ignore