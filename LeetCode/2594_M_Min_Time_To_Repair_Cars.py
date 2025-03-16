import math
from typing import List
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(t):
            total_cars = sum(math.isqrt(t // r) for r in ranks)
            return total_cars >= cars

        low, high = 1, max(ranks) * cars * cars
        while low < high:
            mid = (low + high) // 2
            if canRepairInTime(mid): high = mid
            else: low = mid + 1
        return low