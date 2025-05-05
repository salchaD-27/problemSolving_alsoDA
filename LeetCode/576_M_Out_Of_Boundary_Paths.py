from functools import lru_cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        def dfs(i, j, moves_left):
            if i < 0 or i >= m or j < 0 or j >= n: return 1
            if moves_left == 0: return 0
            paths = 0
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                paths += dfs(i + dx, j + dy, moves_left - 1)
                paths %= MOD
            return paths
        return dfs(startRow, startColumn, maxMove)