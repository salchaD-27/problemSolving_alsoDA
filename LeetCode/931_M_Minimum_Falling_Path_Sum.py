# from typing import List
# from collections import deque
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         n = len(matrix)
#         queue = deque()
#         for col in range(n):
#             queue.append((0, col, matrix[0][col]))
#         min_sum = float('inf')
#         while queue:
#             row, col, path_sum = queue.popleft()
#             if row == n - 1:
#                 min_sum = min(min_sum, path_sum)
#                 continue
#             for dcol in [-1, 0, 1]:
#                 new_col = col + dcol
#                 if 0 <= new_col < n:
#                     queue.append((row + 1, new_col, path_sum + matrix[row + 1][new_col]))
#         return min_sum

from typing import List
class Solution:
    def minFallingPathSumHelper(self, A, row, col, dp):
        m, n = len(A), len(A[0])
        if dp[row][col] != float('inf'): return dp[row][col]
        if row == m - 1: return A[row][col]
        left = right = float('inf')
        if col > 0: left = self.minFallingPathSumHelper(A, row + 1, col - 1, dp)
        straight = self.minFallingPathSumHelper(A, row + 1, col, dp)
        if col < n - 1: right = self.minFallingPathSumHelper(A, row + 1, col + 1, dp)
        dp[row][col] = min(left, min(straight, right)) + A[row][col]
        return dp[row][col]
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        if m == 1 or n == 1: return A[0][0]
        dp = [[float('inf')] * n for _ in range(m)]
        ans = float('inf')
        for i in range(len(A)):
            ans = min(ans, self.minFallingPathSumHelper(A, 0, i, dp))
        return ans