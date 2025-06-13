from typing import List
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i + 1) for i in range(query_row + 2)]
        dp[0][0] = poured
        for r in range(query_row + 1):
            for c in range(len(dp[r])):
                overflow = (dp[r][c] - 1) / 2.0
                if overflow > 0:
                    dp[r + 1][c] += overflow
                    dp[r + 1][c + 1] += overflow
        return min(1, dp[query_row][query_glass])