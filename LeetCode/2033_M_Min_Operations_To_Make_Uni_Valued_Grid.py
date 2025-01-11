from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = [val for row in grid for val in row]
        remainder = flattened[0] % x
        if any(val % x != remainder for val in flattened): return -1

        flattened.sort()
        median = flattened[len(flattened) // 2]
        steps = sum(abs(val - median) // x for val in flattened)
        return steps