# egg doesn’t break - k eggs m-1 moves
# egg breaks - k-1 eggs m-1 moves
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i] = max floors checkable with i eggs and current moves
        dp = [0] * (k + 1)
        m = 0
        while dp[k] < n:
            m += 1
            for eggs in range(k, 0, -1):
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
        return m