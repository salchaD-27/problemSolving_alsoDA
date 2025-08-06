from functools import lru_cache
class Solution:
    def knightDialer(self, n: int) -> int:
        @lru_cache(None)
        def helper(n, row, col):
            if n==0:
                return 1
            ans=0
            for row_i, col_i in [[2,1], [1,2], [-2,1], [-1,2], [2,-1], [1,-2], [-2,-1], [-1,-2]]:
                new_row = row+row_i
                new_col = col+col_i
                if (-1<new_row<3 and -1<new_col<3) or (new_row==3 and new_col==1): ans+=helper(n-1, new_row, new_col)
            return ans%(10**9+7)
        
        ans = helper(n-1, 3, 1)
        for row in range(3):
            for col in range(3):
                ans += helper(n-1, row, col)
        return ans%(10**9+7)
    
class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1 for _ in range(10)]
        for steps in range(0, n - 1):
            n = dp[:]
            dp[0] = n[4] + n[6]
            dp[1] = n[6] + n[8]
            dp[2] = n[7] + n[9]
            dp[3] = n[4] + n[8]
            dp[4] = n[3] + n[9] + n[0]
            dp[5] = 0
            dp[6] = n[1] + n[7] + n[0]
            dp[7] = n[2] + n[6]
            dp[8] = n[1] + n[3]
            dp[9] = n[2] + n[4]
            dp = [num % mod for num in dp]
        return sum(dp) % mod