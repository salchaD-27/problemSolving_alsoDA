from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[i]==nums[j]):
                    if((i*j)%k==0): count+=1
        return count
    
from typing import List
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def calculate(arr, k):
            tempCount=0
            for i in range(len(arr)-1):
                for j in range(i+1, len(arr)):
                    if(arr[i]*arr[j])%k==0: tempCount+=1
            return tempCount
        indexMap={}
        for i in range(len(nums)):
            if nums[i] not in indexMap: indexMap[nums[i]]=[i]
            else: indexMap[nums[i]]+=[i]
        count=0
        for key,val in indexMap.items():
            if(len(val)<2): continue
            elif(len(val)>2): count+=calculate(val, k)
            else:
                if(val[0]*val[1])%k==0: count+=1
        return count