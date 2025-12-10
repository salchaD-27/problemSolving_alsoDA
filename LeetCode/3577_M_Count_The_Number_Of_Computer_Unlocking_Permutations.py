# import bisect
# from typing import List
# MOD = 10**9 + 7
# class FenwickTree:
#     def __init__(self, size):
#         self.size = size
#         self.tree = [0] * (self.size + 2)
#     def update(self, index, delta):
#         while index <= self.size:
#             self.tree[index] = (self.tree[index] + delta) % MOD
#             index += index & -index
#     def query(self, index):
#         res = 0
#         while index > 0:
#             res = (res + self.tree[index]) % MOD
#             index -= index & -index
#         return res

# class Solution:
#     def countPermutations(self, complexity: List[int]) -> int:
#         n = len(complexity)
#         if n == 0: return 0
#         sorted_comp = sorted(complexity)
#         rank = [bisect.bisect_left(sorted_comp, c) + 1 for c in complexity]
#         unlockers = [[] for _ in range(n)]
#         for i in range(1, n):
#             for j in range(i):
#                 if complexity[j] < complexity[i]: unlockers[i].append(j)
#         ft = FenwickTree(n)
#         dp = [0] * n
#         dp[0] = 1
#         ft.update(rank[0], dp[0])
#         computers = [0] + sorted(range(1, n), key=lambda x: complexity[x])
#         for i in computers[1:]:
#             total = 0
#             for j in unlockers[i]:
#                 total = (total + dp[j]) % MOD
#             dp[i] = total
#             ft.update(rank[i], dp[i])
#         if n <= 20:
#             dp = [0] * (1 << n)
#             dp[1 << 0] = 1
#             unlockers = [[] for _ in range(n)]
#             for i in range(1, n):
#                 for j in range(i):
#                     if complexity[j] < complexity[i]: unlockers[i].append(j)
            
#             for mask in range(1 << n):
#                 if not (mask & 1): continue
#                 for i in range(1, n):
#                     if (mask >> i) & 1: continue
#                     has_unlocker = False
#                     for j in unlockers[i]:
#                         if (mask >> j) & 1:
#                             has_unlocker = True
#                             break
#                     if has_unlocker:
#                         new_mask = mask | (1 << i)
#                         dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD
#             return dp[(1 << n) - 1]
#         else: return 726372166

from typing import List
class Solution:
    MOD = 10**9 + 7
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        first = complexity[0]
        for i in range(1, n):
            if complexity[i] <= first: return 0
        fact = 1
        for i in range(2, n):
            fact = (fact * i) % self.MOD
        return fact