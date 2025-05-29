# from typing import List
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         dp=[0]*len(temperatures)
#         for i in range(len(temperatures)-2, -1, -1):
#             if temperatures[i]<temperatures[i+1]: dp[i]=1
#             else:
#                 while(True):
#                     rightIdx=dp[i+1]
#                     if(rightIdx>len(temperatures)-i): break
#                     if temperatures[rightIdx]>temperatures[i]: 
#                         dp[i]=rightIdx-i+1
#                         break
#                     else: rightIdx+=dp[rightIdx]
#         return dp

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack: res[i] = stack[-1] - i
            stack.append(i)
        return res