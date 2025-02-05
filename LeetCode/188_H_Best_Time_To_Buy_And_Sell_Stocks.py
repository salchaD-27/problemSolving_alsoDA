# from typing import List
# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         def bigger(val, arr): return any(x > val for x in arr)

#         if not prices or k == 0: return 0
#         daysToBuy = []
#         for i in range(len(prices) - 1):
#             if bigger(prices[i], prices[i + 1:]): daysToBuy.append((prices[i], i))
#         if len(daysToBuy) > k:
#             daysToBuy.sort()  
#             daysToBuy = daysToBuy[:k]
#         profit = 0
#         sellDays = sorted(daysToBuy, key=lambda x: x[1])
#         for buy_price, idx in sellDays:
#             sell_price = max(prices[idx + 1:])
#             profit += max(sell_price - buy_price, 0)
#         return profit

from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0: return 0
        n = len(prices)
        if k >= n // 2: return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            maxDiff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j])
        return dp[k][-1]