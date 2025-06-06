# from typing import List
# class Solution:
#     def minSwapsCouples(self, row: List[int]) -> int:
#         def getPartnerDist(i):
#             partner=row[i]+1 if row[i]%2==0 else row[i]-1
#             currStep=1
#             while True:
#                 if i-currStep>=0 and row[i-currStep]==partner: return i-currStep
#                 elif i+currStep<=len(row) and row[i+currStep]==partner: return i+currStep
#                 else: currStep+=1

#         dp=[0]*len(row)
#         for i in range(1, len(dp)-1):
#             partner=row[i]+1 if row[i]%2==0 else row[i]-1
#             if row[i-1]==partner or row[i+1]==partner: dp[i]=0
#             else: dp[i]=getPartnerDist(i)

from typing import List
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        for i in range(0, len(row), 2):
            x = row[i]
            y = x ^ 1
            if row[i+1] != y:
                partner_index = pos[y]
                row[i+1], row[partner_index] = row[partner_index], row[i+1]
                pos[row[partner_index]] = partner_index
                pos[row[i+1]] = i+1
                swaps += 1
        return swaps