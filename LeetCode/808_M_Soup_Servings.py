from functools import lru_cache
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000: return 1.0
        n = (n + 24) // 25

        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0: return 0.5  # both empty
            if a <= 0: return 1.0  # a empty first
            if b <= 0: return 0.0  # b is empty first
            return 0.25 * (
                dp(a - 4, b) +       # 100 A, 0 B
                dp(a - 3, b - 1) +   # 75 A, 25 B
                dp(a - 2, b - 2) +   # 50 A, 50 B
                dp(a - 1, b - 3)     # 25 A, 75 B
            )
        return dp(n, n)