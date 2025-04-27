# from collections import Counter
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         res=0
#         count=Counter(s)
#         if(max(count.values())<2): return 1
#         for val in count.values():
#             if val%2==0: res+=val
#         return res

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]: dp[i][j] = 2 + dp[i+1][j-1]
                else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]