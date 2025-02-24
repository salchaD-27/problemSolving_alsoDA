# class Solution:
#     def integerBreak(self, n: int) -> int:
#         def calcDP(dp, val):
#             res=0
#             for i in reversed(range(1, val)):
#                 res=max(res, i*dp[val-i], i*(val-i))
#             return res

#         dp=[0,0,1,2]
#         if(n<4): return dp[n]
#         for i in reversed(range(4, n)):
#             dp.append(calcDP(dp, n-i))
#         return dp[-1]

# class Solution:
#     def integerBreak(self, n: int) -> int:
#         def calcDP(dp, val):
#             res = 0
#             for i in range(1, val):
#                 res = max(res, i * dp[val - i])
#             return res

#         dp = [0] * (n + 1)
#         dp[2]=1
#         for i in range(3, n + 1):
#             dp[i] = max(i, calcDP(dp, i))
#         return dp[n]

class Solution:
    def integerBreak(self, n: int) -> int:
        def calcDP(dp, val):
            res = 0
            for i in range(1, val):
                res = max(res, i * max(val - i, dp[val - i]))
            return res

        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = calcDP(dp, i)
        return dp[n]