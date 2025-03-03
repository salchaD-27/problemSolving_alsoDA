from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        resL=[]
        resG=[]
        count=0
        for i in range(len(nums)):
            if(nums[i]<pivot): resL.append(nums[i])
            elif(nums[i]>pivot): resG.append(nums[i])
            else: count+=1
        return resL+[pivot]*count+resG