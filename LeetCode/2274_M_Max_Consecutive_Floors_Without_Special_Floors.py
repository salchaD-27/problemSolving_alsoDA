# from typing import List

# class Solution:
#     def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
#         res = []       
#         temp = []      
#         j = 0          
#         special.sort() 
#         for i in range(bottom, top + 1):
#             if j < len(special) and i == special[j]:
#                 if len(temp) > len(res): res = temp
#                 temp = []
#                 j += 1  
#             else: temp.append(i)
#         if len(temp) > len(res):
#             res = temp
#         return len(res)


from typing import List

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        ans = 0
        special.sort()
        ans = max(ans, special[0] - bottom)
        for i in range(1, len(special)):
            ans = max(ans, special[i] - special[i - 1] - 1)
        ans = max(ans, top - special[-1])
        return ans