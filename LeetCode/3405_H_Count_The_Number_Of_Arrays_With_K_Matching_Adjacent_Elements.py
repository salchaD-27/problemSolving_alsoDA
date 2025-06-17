# MOD = 10**9 + 7
# class Solution:
#     def countGoodArrays(self, n: int, m: int, k: int) -> int:
#         # building arr of len i with j equal adjacents
#         dp = [[0] * (k + 2) for _ in range(n + 1)]
#         dp[1][0] = m  # first elem has m choices, no adjacent yet
#         for i in range(2, n + 1):
#             for j in range(0, min(i, k + 1)):
#                 # case1: same
#                 dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j]) % MOD
#                 # case2: different
#                 dp[i][j] = (dp[i][j] + dp[i - 1][j] * (m - 1)) % MOD
#         return dp[n][k]

# MOD = 10**9 + 7
# class Solution:
#     def countGoodArrays(self, n: int, m: int, k: int) -> int:
#         prev = [0] * (k + 2)
#         prev[0] = m
#         for i in range(2, n + 1):
#             curr = [0] * (k + 2)
#             for j in range(0, min(i, k + 1)):
#                 curr[j + 1] = (curr[j + 1] + prev[j]) % MOD
#                 curr[j] = (curr[j] + prev[j] * (m - 1)) % MOD
#             prev = curr
#         return prev[k]

MOD = 10**9 + 7
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        max_n = n
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
        for i in range(max_n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        def comb(a, b):
            if b < 0 or b > a: return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        ways = m
        ways = ways * comb(n - 1, k) % MOD
        ways = ways * pow(m - 1, n - 1 - k, MOD) % MOD
        return ways