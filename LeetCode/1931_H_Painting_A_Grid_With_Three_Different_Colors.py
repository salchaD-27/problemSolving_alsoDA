MOD = 10**9 + 7
from itertools import product
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def is_valid(col):
            for i in range(1, m):
                if col[i] == col[i-1]: return False
            return True
        colors = [0, 1, 2]  # R, G, B
        all_patterns = [p for p in product(colors, repeat=m) if is_valid(p)]
        transitions = {p: [] for p in all_patterns}
        for p1 in all_patterns:
            for p2 in all_patterns:
                if all(a != b for a, b in zip(p1, p2)): transitions[p1].append(p2)
        dp = {p: 1 for p in all_patterns}
        for _ in range(n - 1):
            new_dp = {p: 0 for p in all_patterns}
            for p1 in all_patterns:
                for p2 in transitions[p1]:
                    new_dp[p2] = (new_dp[p2] + dp[p1]) % MOD
            dp = new_dp
        return sum(dp.values()) % MOD