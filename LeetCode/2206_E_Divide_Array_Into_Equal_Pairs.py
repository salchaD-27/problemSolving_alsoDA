from typing import List
from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res=0
        count=Counter(nums)
        for val in count.values():
            if val>=2: res+=val//2
        return True if res>=len(nums)/2 else False