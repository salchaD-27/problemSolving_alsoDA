from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res=set()
        for i in range(len(nums)-1):
            currValue=nums[i]
            kLess=currValue-k
            kMore=currValue+k
            if(kLess in nums[i+1:]): res.add((kLess, currValue))
            if(kMore in nums[i+1:]): res.add((currValue, kMore))
        return len(res)
    
from typing import List
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        c = Counter(nums)
        if k == 0:
            for key, val in c.items():
                if val>1: cnt +=1
        else:
            for key, val in c.items():
                if k+key in c: cnt+=1
        return cnt