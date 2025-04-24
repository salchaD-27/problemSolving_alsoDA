# from typing import List
# class Solution:
#     def predictTheWinner(self, nums: List[int]) -> bool:
#         def countScore(currScore1, currScore2, lastChance, remArr):
#             if not remArr: return currScore1>currScore2
#             if(lastChance==2):
#                 return countScore(currScore1+nums[0], currScore2, 1, nums[1:]) or countScore(currScore1+nums[-1], currScore2, 1, nums[:-1])
#             elif(lastChance==1):
#                 return countScore(currScore1, currScore2+nums[0], 2, nums[1:]) or countScore(currScore1, currScore2+nums[-1], 2, nums[:-1])
#         return countScore(nums[0], 0, 1, nums[1:]) or countScore(nums[-1], 0, 1, nums[:-1])

from typing import List
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][n-1] >= 0