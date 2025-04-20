import math
from collections import Counter
class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = Counter(answers)
        rabbits = 0
        for x, freq in count.items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            rabbits += groups * group_size
        return rabbits
    
from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        c = Counter(answers)
        for k, v in c.items():
            q, r = divmod(v, k+1)
            ans += q*(k+1) + ((k+1) if r > 0 else 0)
        return ans