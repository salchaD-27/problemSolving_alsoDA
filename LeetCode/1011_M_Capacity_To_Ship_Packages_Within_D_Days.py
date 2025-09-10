from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high=max(weights),sum(weights)
        while low<=high:
            mid=(low+high)//2
            sumt=1
            ctr=0
            for i in weights:
                if ctr+i>mid:
                    sumt+=1
                    ctr=i
                else: ctr+=i
            if sumt<=days: high=mid-1
            else: low=mid+1
        return low