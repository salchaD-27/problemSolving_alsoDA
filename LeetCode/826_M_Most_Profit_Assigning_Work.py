from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        res = 0
        max_profit = 0
        j = 0
        for ability in worker:
            while j < len(jobs) and jobs[j][0] <= ability:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            res += max_profit
        return res