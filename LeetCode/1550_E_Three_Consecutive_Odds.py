from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if(len(arr)<3): return False
        for i in range(1, len(arr)-1):
            if(arr[i-1]%2!=0 and arr[i]%2!=0 and arr[i+1]%2!=0): return True
        return False