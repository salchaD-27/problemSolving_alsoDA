# from typing import List
# class Solution:
#     def minimumLines(self, stockPrices: List[List[int]]) -> int:
#         prevX=stockPrices[1][0]
#         prevY=stockPrices[1][1]
#         prevSlope=abs((stockPrices[1][1]-stockPrices[0][1])/(stockPrices[1][0]-stockPrices[0][0]))
#         lines=1
#         for i in range(2, len(stockPrices)):
#             X=stockPrices[i][0]
#             Y=stockPrices[i][1]
#             slope=abs((Y-prevY)/(X-prevX))
#             if(slope!=prevSlope): lines+=1
#             prevX=X
#             prevY=Y
#             prevSlope=slope
#         return lines

from typing import List
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        if len(stockPrices) <= 1: return 0
        prevX, prevY = stockPrices[1][0], stockPrices[1][1]
        prevSlopeNum = stockPrices[1][1] - stockPrices[0][1]
        prevSlopeDen = stockPrices[1][0] - stockPrices[0][0]
        lines = 1
        for i in range(2, len(stockPrices)):
            X, Y = stockPrices[i][0], stockPrices[i][1]
            slopeNum = Y - prevY
            slopeDen = X - prevX
            if slopeNum * prevSlopeDen != slopeDen * prevSlopeNum: lines+=1
            prevX, prevY = X, Y
            prevSlopeNum, prevSlopeDen = slopeNum, slopeDen
        return lines