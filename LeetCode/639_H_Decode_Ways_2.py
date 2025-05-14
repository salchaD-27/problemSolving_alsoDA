# class Solution:
#     def numDecodings(self, s: str) -> int:
#         MOD=10**9+7
#         dp=[1]*len(s)
#         if s[0]=='*': dp[0]=9
#         for i in range(1, len(dp)):
#             if(s[i]!='*'):
#                 if(0<int(s[i])<=6 and int(s[i-1])==2): dp[i]=2
#                 elif(0<int(s[i]) and int(s[i-1])==1): dp[i]=2
#                 else: dp[i]=1
#             else: dp[i]=9
#         prod=1
#         for i in range(len(dp)):
#             prod*=dp[i]
#         return prod%MOD

class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] == '*': dp[1] = 9
        elif s[0] != '0': dp[1] = 1
        for i in range(2, n + 1):
            first = s[i - 1]
            second = s[i - 2]
            # 1char
            if first == '*': dp[i] += 9 * dp[i - 1]
            elif first != '0': dp[i] += dp[i - 1]
            # 2char
            if second == '*':
                if first == '*': dp[i] += 15 * dp[i - 2]  # 11-19 and 21-26
                elif '0' <= first <= '6': dp[i] += 2 * dp[i - 2]  # 1x and 2x
                else: dp[i] += dp[i - 2]  # 1x only
            elif second == '1':
                if first == '*': dp[i] += 9 * dp[i - 2]  # 11-19
                else: dp[i] += dp[i - 2]
            elif second == '2':
                if first == '*': dp[i] += 6 * dp[i - 2]  # 21-26
                elif '0' <= first <= '6': dp[i] += dp[i - 2]
            dp[i] %= MOD
        return dp[n]