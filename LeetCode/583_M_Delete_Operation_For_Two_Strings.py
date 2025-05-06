class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]: dp[i + 1][j + 1] = dp[i][j] + word1[i]
                else: dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
        lcs=dp[m][n]
        return m-len(lcs)+n-len(lcs)