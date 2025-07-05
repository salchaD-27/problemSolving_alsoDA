from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        numMap={}
        for i in range(len(arr)):
            if arr[i] in numMap: numMap[arr[i]]+=1
            else: numMap[arr[i]]=1
        lucky=-1
        for num in numMap:
            if numMap[num]==num: lucky=max(lucky,num)
        return lucky