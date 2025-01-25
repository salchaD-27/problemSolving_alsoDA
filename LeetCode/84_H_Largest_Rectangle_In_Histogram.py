# from typing import List
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         def area(i, heights):
#             L=R=i
#             while(R+1<len(heights) and heights[R+1]>=heights[i]): R+=1
#             while(L-1>=0 and heights[L-1]>=heights[i]): L-=1
#             return heights[i]*(R-L+1)
#         ans=0
#         for i in range(len(heights)):
#             ans=max(ans, area(i, heights))
#         return ans

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area