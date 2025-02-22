# from typing import List
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         if not matrix or not matrix[0]: return 0  
#         rows, cols = len(matrix), len(matrix[0])
#         dp = [[1] * cols for _ in range(rows)]
#         for i in reversed(range(rows)):
#             for j in reversed(range(cols)):
#                 if j + 1 < cols and matrix[i][j] < matrix[i][j + 1]: dp[i][j] = max(dp[i][j], dp[i][j + 1] + 1)
#                 if i + 1 < rows and matrix[i][j] < matrix[i + 1][j]: dp[i][j] = max(dp[i][j], dp[i + 1][j] + 1)
#         for i in range(rows):
#             for j in range(cols):
#                 if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]: dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
#                 if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]: dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
#         return max(max(row) for row in dp)

from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if dp[i][j] != -1: return dp[i][j] 
            max_len = 1 
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]: max_len = max(max_len, 1 + dfs(x, y))
            dp[i][j] = max_len 
            return max_len
        
        if not matrix or not matrix[0]: return 0
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)] 
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]  
        return max(dfs(i, j) for i in range(rows) for j in range(cols))