from typing import List
from itertools import product
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)    
        temp=list(product(['0', '1'], repeat=n))
        for val in temp:
            s=''.join(list(val))
            if(s not in nums): return s