from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp=nums1+nums2
        temp.sort()
        if(len(temp)%2==0): return (temp[len(temp)//2]+temp[len(temp)//2 -1])/2
        else: return temp[len(temp)//2]