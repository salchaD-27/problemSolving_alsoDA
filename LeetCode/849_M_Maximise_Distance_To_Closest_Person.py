# from typing import List
# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         inc=[0]*len(seats)
#         inc[0]=float('inf') if seats[0]==0 else 0
#         dec=[0]*len(seats)
#         dec[0]=float('inf') if seats[0]==0 else 0
#         for i in range(1, len(seats)):
#             if seats[i]==0: inc[i]=inc[i-1]+1
#             else: inc[i]=0
#         for i in range(len(seats)-2, -1, -1):
#             if seats[i]==0: dec[i]=dec[i+1]+1
#             else: dec[i]=0
#         res=0
#         for i in range(len(inc)):
#             if inc[i]!=float('inf') and dec[i]!=float('inf'): res=max(res, min(inc[i],dec[i]))
#             elif inc[i]==float('inf') and dec[i]!=float('inf'): res=max(res, dec[i])
#             else: res=max(res, inc[i])
#         return res

from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        inc = [n] * n
        dec = [n] * n
        if seats[0] == 1: inc[0] = 0
        for i in range(1, n):
            if seats[i] == 1: inc[i] = 0
            else: inc[i] = inc[i - 1] + 1
        if seats[-1] == 1: dec[-1] = 0
        for i in range(n - 2, -1, -1):
            if seats[i] == 1: dec[i] = 0
            else: dec[i] = dec[i + 1] + 1
        res = 0
        for i in range(n):
            if seats[i] == 0: res = max(res, min(inc[i], dec[i]))
        return res

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        index = -1
        ans = 1
        for i in range(len(seats)): 
            if seats[i] == 1: 
                if index == -1: 
                    ans = max(ans, i)
                    index = i
                else: 
                    ans = max(ans, (i-index)//2)
                    index = i
        ans = max(ans, len(seats)-1-index)
        return ans