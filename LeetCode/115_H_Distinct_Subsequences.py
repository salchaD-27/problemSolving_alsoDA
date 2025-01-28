# import math
# from typing import List
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         def nCr(n, r):
#             if n < r: return 0
#             return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

#         s_charDict = {char: 0 for char in t}
#         t_charDict = {char: t.count(char) for char in t}
#         for i in range(len(s)):
#             if s[i] in s_charDict: s_charDict[s[i]] += 1
#         ans = 1
#         for key in t_charDict:
#             ans *= nCr(s_charDict[key], t_charDict[key])
#         return ans

from typing import List
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]: dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else: dp[i][j] = dp[i - 1][j]
        return dp[m][n]