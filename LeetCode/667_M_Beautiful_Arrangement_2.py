from typing import List
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        low, high = 1, k + 1
        while low <= high:
            if low == high:
                res.append(low)
                break
            res.append(low)
            res.append(high)
            low += 1
            high -= 1
        for i in range(k + 2, n + 1):
            res.append(i)
        return res