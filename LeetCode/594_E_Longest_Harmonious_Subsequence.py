from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numbers={}
        for i in range(len(nums)):
            if nums[i] not in numbers: numbers[nums[i]]=1
            else: numbers[nums[i]]+=1
        res=0
        for num in numbers:
            if num-1 in numbers: res=max(res, numbers[num-1]+numbers[num])
            if num+1 in numbers: res=max(res, numbers[num]+numbers[num+1])
        return res