# from typing import List
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         digits=len(s)
#         poss=0
#         for i in range(digits-2, -1, -1):
#             # Nums in range 10-26 can form 2 digit num
#             if(0<int(s[i])<=2 and 0<=int(s[i+1])<7): poss+=1
#         return (poss**2)-1

from typing import List
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # Single digit decode
            if s[i - 1] != '0': dp[i] += dp[i - 1]
            # Two digit decode
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26: dp[i] += dp[i - 2]
        return dp[n]