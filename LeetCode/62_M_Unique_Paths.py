# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def traverse(x, y, m, n):
#             if x == m - 1 and y == n - 1: return 1
#             if x >= m or y >= n: return 0
#             return traverse(x + 1, y, m, n) + traverse(x, y + 1, m, n)
#         return traverse(0, 0, m, n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]