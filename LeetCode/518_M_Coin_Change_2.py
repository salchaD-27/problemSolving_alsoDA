# from typing import List
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         def subChange(remAmount):
#             count=0
#             for i in range(len(coins)):
#                 if(remAmount-coins[i]>0): count+=subChange(remAmount-coins[i])
#                 elif(remAmount-coins[i]==0): count+=1
#             return count
#         return subChange(amount)

from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]