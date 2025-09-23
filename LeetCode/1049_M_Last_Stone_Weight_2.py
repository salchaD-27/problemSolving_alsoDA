from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #Memoization
        def findMaxTarget(start, targetSum, dp):
            if start < 0 or targetSum == 0: return 0
            if dp[start][targetSum] != -1: return dp[start][targetSum]
            if targetSum >= stones[start]: dp[start][targetSum] = max(findMaxTarget(start - 1, targetSum, dp), stones[start] + findMaxTarget(start - 1, targetSum - stones[start], dp))
            else: dp[start][targetSum] = findMaxTarget(start - 1, targetSum, dp)
            return dp[start][targetSum]

        l = len(stones)
        totalSum = 0
        for s in stones:
            totalSum += s

        target = totalSum // 2
        dp = [[-1] * (target + 1) for _ in range(l+1)]
        maxSum = findMaxTarget(l - 1, target, dp)
        return totalSum - maxSum - maxSum