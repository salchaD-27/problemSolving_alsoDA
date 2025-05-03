# from typing import List
# class Solution:
#     def removeBoxes(self, boxes: List[int]) -> int:
#         score=0
#         while(boxes):
#             dp=[0]*len(boxes)
#             dp[0]=1
#             for i in range(1,len(boxes)):
#                 if(boxes[i]!=boxes[i-1]): dp[i]=1
#                 else: dp[i]=1+dp[i-1]
#             maxCount=0
#             maxIdx=0
#             for i in range(len(dp)):
#                 if(dp[i]>maxCount):
#                     maxCount=dp[i]
#                     maxIdx=i
#             score+=maxCount**2
#             boxes=boxes[:maxIdx-maxCount+1]+boxes[maxIdx+1:]
#         return score
    
from typing import List
from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(l, r, k):
            if l > r: return 0
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            res = dp(l, r - 1, 0) + (k + 1) ** 2
            for i in range(l, r):
                if boxes[i] == boxes[r]: res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            return res
        return dp(0, len(boxes) - 1, 0)