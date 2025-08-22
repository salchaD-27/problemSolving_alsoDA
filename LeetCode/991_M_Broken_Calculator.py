class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        def helper(s, t):
            if s >= t: return s - t
            return 1 + helper(s, t // 2) if t % 2 == 0 else 1 + helper(s, t + 1)

        return helper(startValue, target)