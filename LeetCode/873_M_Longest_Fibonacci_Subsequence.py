# from typing import List
# class Solution:
#     def lenLongestFibSubseq(self, arr: List[int]) -> int:
#         arrSet=set(arr)
#         res=0
#         for i in range(len(arr)-1):
#             for j in range(i+1, len(arr)):
#                 prev,curr=arr[i],arr[j]
#                 next=prev+curr
#                 temp=2
#                 while next in arrSet:
#                     prev,curr=curr,next
#                     next=prev+curr
#                     temp+=1
#                     res=max(res, temp)
#         return res
    
from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arrMap = {n:i for i,n in enumerate(arr)}
        res=0
        dp={}
        for i in reversed(range(len(arr)-1)):
            for j in reversed(range(i+1, len(arr))):
                prev,curr=arr[i],arr[j]
                next=prev+curr
                temp=2
                if next in arrMap:
                    temp=1+dp[(j, arrMap[next])]
                    res=max(res, temp)
                dp[(i,j)]=temp
        return res