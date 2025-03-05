class Solution:
    def coloredCells(self, n: int) -> int:
        def helper(n): return ((n+1)**2)//4
        return 2*helper(2*n-1)-(2*n-1)