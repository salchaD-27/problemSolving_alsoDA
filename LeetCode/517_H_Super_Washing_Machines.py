from typing import List
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0: return -1
        target = total // n
        max_moves = 0
        cumulative_diff = 0
        for i in range(n):
            diff = machines[i] - target
            cumulative_diff += diff
            max_moves = max(max_moves, abs(cumulative_diff), diff)
        return max_moves