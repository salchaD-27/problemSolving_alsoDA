from heapq import heappush, heappop
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1] 
        seen = set(heap) 
        for _ in range(n):
            curr_ugly = heappop(heap) 
            for prime in primes: 
                new_ugly = curr_ugly * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)
        return curr_ugly 