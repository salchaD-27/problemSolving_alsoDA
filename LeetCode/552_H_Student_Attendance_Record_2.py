# from functools import lru_cache
# class Solution:
#     def checkRecord(self, n: int) -> int:
#         MOD = 10**9 + 7
#         @lru_cache(None)
#         def subRecord(pos: int, absents: int, lates: int) -> int:
#             if absents >= 2 or lates >= 3: return 0
#             if pos == n: return 1
#             # adding P
#             total = subRecord(pos + 1, absents, 0)
#             # adding A
#             total += subRecord(pos + 1, absents + 1, 0)
#             # adding L
#             total += subRecord(pos + 1, absents, lates + 1)
#             return total % MOD
#         return subRecord(0, 0, 0)
    
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0]*3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            new_dp = [[0]*3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    val = dp[a][l]
                    if val == 0: continue
                    # adding P
                    new_dp[a][0] = (new_dp[a][0] + val) % MOD
                    # adding A
                    if a < 1: new_dp[a+1][0] = (new_dp[a+1][0] + val) % MOD
                    # adding L
                    if l < 2: new_dp[a][l+1] = (new_dp[a][l+1] + val) % MOD
            dp = new_dp
        return sum(dp[a][l] for a in range(2) for l in range(3)) % MOD