from itertools import combinations as cm
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs=list(cm(range(1,10), k))
        ans=[]
        for comb in combs:
            if(sum(comb)==n): ans.append(comb)
        return ans