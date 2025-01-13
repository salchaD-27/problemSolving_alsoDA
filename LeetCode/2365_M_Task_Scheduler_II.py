from typing import List
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_day = {} 
        days = 0      
        for task in tasks:
            days += 1 
            if task in last_day:
                if days - last_day[task] <= space: days = last_day[task] + space + 1
            last_day[task] = days
        return days