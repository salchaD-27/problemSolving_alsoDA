from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n=len(tops)
        count={}
        for i in range(n):
            if tops[i] not in count: count[tops[i]]=1
            else: count[tops[i]]+=1
        for i in range(n):
            if bottoms[i] not in count: count[bottoms[i]]=1
            else: count[bottoms[i]]+=1
        possEquals=[]
        for val,freq in count.items():
            if freq>=n: possEquals.append(val)
        res=float('inf')
        for i in range(len(possEquals)):
            topReq=bottomReq=0
            for j in range(len(tops)):
                if(tops[j]!=possEquals[i] and bottoms[j]==possEquals[i]): topReq+=1
                elif(tops[j]!=possEquals[i] and bottoms[j]!=possEquals[i]): 
                    topReq=-1
                    break
                else: continue
            for j in range(len(bottoms)):
                if(bottoms[j]!=possEquals[i] and tops[j]==possEquals[i]): bottomReq+=1
                elif(bottoms[j]!=possEquals[i] and tops[j]!=possEquals[i]): 
                    bottomReq=-1
                    break
                else: continue
            res=min(res,topReq if topReq!=-1 else float('inf'),bottomReq if bottomReq!=-1 else float('inf'))
        return res if res!=float('inf') else -1
    
from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x: return float('inf')  # imposs
                elif tops[i] != x: rotations_top += 1
                elif bottoms[i] != x: rotations_bottom += 1
            return min(rotations_top, rotations_bottom)
        candidate1 = tops[0]
        candidate2 = bottoms[0]
        ans = min(check(candidate1), check(candidate2) if candidate1 != candidate2 else float('inf'))
        return -1 if ans == float('inf') else ans