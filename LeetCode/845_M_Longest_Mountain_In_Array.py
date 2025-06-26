from typing import List
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3: return 0
        inc = [1] * n
        dec = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]: inc[i] = inc[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]: dec[i] = dec[i + 1] + 1
        maxLen = 0
        for i in range(1, n - 1):
            if inc[i] > 1 and dec[i] > 1: maxLen = max(maxLen, inc[i] + dec[i] - 1)
        return maxLen