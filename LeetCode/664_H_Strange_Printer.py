# class Solution:
#     def strangePrinter(self, s: str) -> int:
#         if len(s)>1:
#             firstChar=s[0]
#             firstCharLastIdx=-1
#             for i in reversed(range(1,len(s))):
#                 if s[i]==firstChar:
#                     firstCharLastIdx=i
#                     break
#             return 1+self.strangePrinter(s[1:firstCharLastIdx])+self.strangePrinter(s[firstCharLastIdx+1:])
#         return 1

class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        s = ''.join([s[i] for i in range(n) if i == 0 or s[i] != s[i-1]])
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                dp[i][j] = dp[i+1][j] + 1
                for k in range(i+1, j+1):
                    if s[i] == s[k]: dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k][j])
        return dp[0][n-1]