from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for num in arr:
            # new ORs ending at curr idx
            new_cur = {num | x for x in cur} | {num}
            cur = new_cur
            res |= cur
        return len(res)