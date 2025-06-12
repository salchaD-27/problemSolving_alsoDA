class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x):
            res = 0
            while x > 0:
                x //= 5
                res += x
            return res
        def leftBound(k):
            lo, hi = 0, 5 * (k + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                if f(mid) < k: lo = mid + 1
                else: hi = mid
            return lo
        def rightBound(k):
            lo, hi = 0, 5 * (k + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                if f(mid) <= k: lo = mid + 1
                else: hi = mid
            return lo
        return rightBound(k) - leftBound(k)