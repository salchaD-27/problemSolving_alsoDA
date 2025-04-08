from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opers=0
        setNums=set(nums)
        while len(setNums)!=len(nums):
            nums=nums[3:]
            setNums=set(nums)
            opers+=1
        return opers