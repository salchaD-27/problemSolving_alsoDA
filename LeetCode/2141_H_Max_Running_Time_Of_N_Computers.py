# from typing import List

# class Solution:
#     def parts(self, val: int, parts: int) -> List[int]:
#         res = []
#         total = 0
#         for i in range(parts - 1):
#             res.append(val//parts)
#             total += val//parts
#         res.append(val - total)
#         return res

#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         batteries.sort()
#         batteries.reverse()
#         compRun = [batteries[i] for i in range(n)]
#         i=n-1
#         while((len(batteries)-1-i)>=n):
#             for j in range(n):
#                 compRun[j]+=batteries[i]
#                 i+=1
#         for i in range(n, len(batteries)):

#             temp = self.parts(batteries[i], n)
#             for j in range(len(temp)):
#                 compRun[j] += temp[j]
#         return min(compRun)
    
from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total_energy = sum(batteries)
        left, right = 0, total_energy // n
        
        while left < right:
            mid = (left + right + 1) // 2 
            required_energy = n * mid 
            available_energy = sum(min(b, mid) for b in batteries)
            if available_energy >= required_energy: left = mid
            else: right = mid - 1
        return left