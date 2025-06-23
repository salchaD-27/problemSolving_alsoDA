# from typing import List
# from itertools import product
# class Solution:
#     def numFactoredBinaryTrees(self, arr: List[int]) -> int:
#         arr.sort()
#         MOD = 10**9 + 7
#         dp = {x: 1 for x in arr}
#         for a, b in product(arr, repeat=2):
#             res = a * b
#             if res in dp:
#                 dp[res] += dp[a] * dp[b]
#                 dp[res] %= MOD
#         return sum(dp.values()) % MOD

from typing import List
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        for i in range(len(arr)):
            x = arr[i]
            dp[x] = 1
            for j in range(i):
                a = arr[j]
                if x % a == 0:
                    b = x // a
                    if b in dp: dp[x] += dp[a] * dp[b]
        
        return sum(dp.values()) % MOD