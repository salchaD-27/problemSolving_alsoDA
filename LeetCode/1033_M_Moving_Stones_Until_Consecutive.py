from typing import List
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        maxi = max(a,b,c) - min(a,b,c) - 2
        mini = max((min(abs(a-b),abs(b-c),abs(a-c), 3) - 1), 1)
        if maxi == 0: mini = 0            
        return [mini,maxi]