from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        def commonTill(i):
            nums={}
            for ii in range(i+1):
                if A[ii] not in nums: nums[A[ii]]=1
                else: nums[A[ii]]+=1
                if B[ii] not in nums: nums[B[ii]]=1
                else: nums[B[ii]]+=1
            res=0
            for num in nums:
                if nums[num]%2==0 : res+=1
            return res
        return [commonTill(i) for i in range(len(A))]

from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_A = set()
        seen_B = set()
        common = set()
        result = []
        for a, b in zip(A, B):
            seen_A.add(a)
            seen_B.add(b)
            if a in seen_B: common.add(a)
            if b in seen_A: common.add(b)
            result.append(len(common))
        return result