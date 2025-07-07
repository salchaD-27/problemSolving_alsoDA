from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low,high=0,len(arr)-1
        while low<high:
            mid=(low+high)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]: return mid
            elif arr[mid-1]<arr[mid]<arr[mid+1]: low=mid
            else: high=mid
        return -1