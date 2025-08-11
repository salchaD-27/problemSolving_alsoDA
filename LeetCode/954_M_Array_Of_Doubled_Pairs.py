from typing import List
from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for x in sorted(arr, key=abs):
            if count[x] == 0: continue
            if count[2 * x] == 0: return False
            count[x] -= 1
            count[2 * x] -= 1
        return True

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for num in sorted(count.keys(), key=abs):  # sort by absolute value for handling negatives
            if count[num] > count[2 * num]: return False
            count[2 * num] -= count[num]
        return True